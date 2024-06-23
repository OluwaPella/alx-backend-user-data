#!/usr/bin/env python3
"""doc doc"""
from flask import request, jsonify
from models import User
import os
@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """POST /api/v1/auth_session/login
    Return:
      - JSON representation of a User object.
    """
    email = request.get('email')
    password = request.get("password")
    if not email:
        return jsonify({"error":"email missing"}), 400
    if not password:
        return jsonify({"eeror": "password missing"}), 400
    user = User.serach({"email": email})
    if  not user:
        return jsonify({"error": "password missing"})
    if not user.is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        user_data = user.to_json()
        response = jsonify(user_data)
        response.set_cookie(os.getenv("SESSION_NAME"), session_id)
        return response
    return jsonify({"error": "wrong password"}), 401
