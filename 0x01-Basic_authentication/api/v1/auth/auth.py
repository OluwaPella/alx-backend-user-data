#!/usr/bin/env python3
"""doc doc """
from typing import List, TypeVar
from flask import request


class Auth:
    """logic for auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """logic that check if auth is required or not"""
        if path is None:
            return True
        if excluded_paths is None or []:
            return True
        if path[-1] != "/":
            if not(path := path + '/'):
                return False

    def authorization_header(self, request=None) -> str:
        """logic that check auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """logic that identify current_user"""
        return None
