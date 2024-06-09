#!/usr/bin/env python3
"""doc doc """
from api.v1.auth.auth import Auth
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

    def decode_base64_authorization_header(self,
        base64_authorization_header: str) -> str:
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
