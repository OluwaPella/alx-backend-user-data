#!/usr/bin/python3 
from flask import request



class auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False - path and excluded_paths
    

    def authorization_header(self, request=None) -> str:
        return  request(None)
    
    def current_user(self, request=None) -> TypeVar('User'):
        return request(None)
    