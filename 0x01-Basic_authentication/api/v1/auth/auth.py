#!/usr/bin/env python3
"""
import 
"""
from flask import request



class auth:
    """logic that designed manage
    user authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """logic that check if auth is required or not
        """
        return False
    

    def authorization_header(self, request=None) -> str:
        """logic that retrieve the authorize header from the
        request
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        logic to identify current user
        """
        return None
    