#!/usr/bin/env python3
"""doc doc"""
from flask import request, jsonify, abort
import os
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """this logic login and create session"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    user_data = User.search({'email': email})
    if not user_data:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_data[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        res = jsonify(user.to_json())
        res.set_cookie(os.getenv('SESSION_NAME'), session_id)
        return res


@app_views.route('/auth_session/logout', methods=['DELETE'])
def logout() -> str:
    """this logic logout and destroy session"""
    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
