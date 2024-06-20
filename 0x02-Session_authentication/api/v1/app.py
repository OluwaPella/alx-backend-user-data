#!/usr/bin/env python3
"""Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
auth_type = getenv('AUTH_TYPE', 'auth')
if auth_type == "basic_auth":
    auth = BasicAuth()
if auth_type == "auth":
    auth = Auth()
if auth_type == "session_auth":
    auth = SessionAuth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """an unauthorize function"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Error handler: Forbidden"""
    return jsonify({"error": "Forbidden"}), 403


excluedd_paths = ['/api/v1/auth_session/login/']
if request.path not in excluedd_paths and (not auth.authorization_header(request) and not auth.session_cookie(request)):
    abort(401)
    

@app.before_request
def before_requests():
    """doc doc"""
    if auth is None:
        return
    if not auth.require_auth(request.path,
                             ['/api/v1/status/',
                              '/api/v1/unauthorized/',
                              '/api/v1/forbidden/']):
        return

    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)
    request.current_user = auth.current_user(request)
   

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
