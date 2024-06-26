#!/usr/bin/env python3
"""session auth"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """this instance method creates a Session ID for a user"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """this instance method returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        else:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """this instance method returns a User
          instance based on a cookie value"""
        session_token = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_token)
        return User.get(user_id)
    
    def destroy_session(self, request=None):
        """this instance method deletes the user session/logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        
        del self.user_id_by_session_id[session_id]
        
        return True