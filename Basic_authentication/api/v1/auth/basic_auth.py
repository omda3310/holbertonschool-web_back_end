#!/usr/bin/env python3
"""basic_auth class"""
from api.v1.auth.auth import Auth
from Base64 import b64decode


class BasicAuth(Auth):
    """Class BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startwith("Basic "):
            return None
        return authorization_header.split(' ', 1)[1]
