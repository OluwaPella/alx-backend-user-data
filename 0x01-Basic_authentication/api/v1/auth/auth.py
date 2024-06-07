#!/usr/bin/env python3
"""
import 
"""
from flask import request



class auth:
    """auth designed to manage
    user authentication api
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ auth checked if authentication will
        be required also check take list of excluded path
        auth wont be necessary
        """
        return False
    

    def authorization_header(self, request=None) -> str:
        """
        this retrieve the authorize header from the
        request
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        logic to identify current user
        """
        return None
    