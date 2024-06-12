#!/usr/bin/env python3
"""doc doc """
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """logic for auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """logic that check if auth is required or not"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
                return True
        for excluded_path in excluded_paths:
             excluded_path =  excluded_path.strip()
             
             checked = ''
             if excluded_path[-1] == '*':
                checked = '{}.*'.format(excluded_path[:-1])
            elif excluded_path[-1] == '/':
                checked = '{}/*'.format(excluded_path[:-1])
            else:
                checked = '{}/*'.format(excluded_path)
            
            if re.match(checked, path):
                return False

            return True

    def authorization_header(self, request=None) -> str:
        """logic that check auth header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """logic that identify current_user"""
        return None
