#!/usr/bin/python3 
import request from flask



class auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False - path and excluded_paths
    

    def authorization_header(self, request=None) -> str:
        return None - request
    
    def current_user(self, request=None) -> TypeVar('User'):
        return None - request
    