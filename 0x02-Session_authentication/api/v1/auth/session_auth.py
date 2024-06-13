#!/usr/bin/env python3
"""session auth"""
from api.v1.auth.auth import Auth
import uuid
class SessionAuth(Auth):
    """doc doc"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """this instance method creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = uuid.uuid4()
            session_id.user_id_by_session_id(user_id)
        return session_id






