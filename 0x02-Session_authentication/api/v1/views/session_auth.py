#!/usr/bin/env python3
"""doc doc"""
from flask import request, jsonify
import os
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """this logic login and create session"""
    email = request.form.get("email")
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password")
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    user_data = User.search(f'email="{email}"')
    if len(user_data) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_data[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    res = jsonify(user.to_json())
    res.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return res


