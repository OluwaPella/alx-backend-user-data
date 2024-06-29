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
    password = request.form.get("password")
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    user_data = User.search('email==email')
    if not user_data:
        return jsonify({"error": "no user found for this email"}), 404
    if user_data[0].is_valid_password(password):
        from api.v1.app import auth
        """create session_id"""
        session_id = auth.create_session(getattr(user_data[0], 'id'))
        re = user_data[0].to_json()
        re.set_cookie(os.getenv("SESSION_NAME"), session_id)
        return re
    return jsonify({"error": "wrong password"}), 401





