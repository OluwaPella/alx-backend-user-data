#!/usr/bin/venv python3
"""session auth"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """this instance method creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            




