#!/usr/bin/env python3
"""doc doc """
from api.v1.auth.auth import Auth
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64 authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """decode base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_byte = base64.b64decode(base64_authorization_header)
            return decoded_byte.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        try:
            email, password = decoded_base64_authorization_header.split(':', 1)
            return email, password
        except ValueError:
            return None

    def user_object_from_credentials(self, user_email: str,
    user_pwd: str) -> TypeVar('User'):
        """this logic retrieves a user object based on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user_data = User.search(email=user_email)
            for user in user_data:
                if user:
                    return user.is_valid_password(user_pwd)
        except Exception:
            return None
