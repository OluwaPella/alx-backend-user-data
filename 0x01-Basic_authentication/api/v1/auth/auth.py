#!/usr/bin/env python3
"""doc doc """
from typing import List, TypeVar
from flask import request


class Auth:
    """logic for auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """logic that check if auth is required or not"""
        return False

    def authorization_header(self, request=None) -> str:
        """logic that check auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """logic that identify current_user"""
        return None
