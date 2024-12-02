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


@app.before_request
def before_requests():
    """
    Checks if authorization is required for the
    requested path. If authorization is required,
    it checks if the Authorization header is present.
    If the Authorization header is not present,
    a 401 error is returned. If the Authorization
    header is present but the user doesn't exist,
    a 403 error is returned.
    """
    # Check if authorization is required

    if not auth.require_auth(request.path,
                             ['/api/v1/status/',
                              '/api/v1/unauthorized/',
                              '/api/v1/forbidden/',
                              '/api/v1/auth_session/login/']):
        return

    # Check if Authorization header is present
    if auth.authorization_header(request) is None:
        abort(401)

    # Check if user exists
    if auth.current_user(request) is None:
        abort(403)

    # Add current user to request object
    request.current_user = auth.current_user(request)

    # Check if session cookie is present for Basic Auth
    if auth.authorization_header(request) and auth.session_cookie(request):
        abort(401)
   

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
