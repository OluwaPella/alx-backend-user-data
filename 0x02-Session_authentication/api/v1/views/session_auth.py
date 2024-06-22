#!/usr/bin/env python3
from flask import request, jsonify
from models import User
from api.v1.app import app
from api.v1.app import auth

"""session auth"""
@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """doc doc"""
    email = request.get('email')
    password = request.get("password")
    if email is None:
        return jsonify({"error":"email missing"}), 400
    if password is None:
        return jsonify({"eeror": "password missing"}), 400
    user = User.serach({"email": email})
    if user is None:
        return jsonify({"error": "password missing"})
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_id = auth.create_session(user.id)
    return jsonify({"session_id": session_id})
    
    