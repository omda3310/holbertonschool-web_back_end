#!/usr/bin/env python3
""" Module Basic Authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic Authentication Class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract Base 64 Authorization """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        enc = authorization_header.split(' ', 1)[1]

        return enc

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Return the decoded value of a Base64.
        """
        if base64_authorization_header is None \
           or not isinstance(base64_authorization_header, str):
            return None

        try:
            code_base64 = base64_authorization_header.encode('utf-8')
            code_message = b64decode(code_base64)
            message = code_message.decode('utf-8')
            return message
        except Exception:
            return None

        def extract_user_credentials(self,
                                     decoded_base64_authorization_header:
                                         str) -> (str, str):
            """
             returns the user email and password from
             the Base64 decoded value.
            """
            if decoded_base64_authorization_header is None:
                return None, None
            if not isinstance(decoded_base64_authorization_header, str):
                return None, None
            if "":" not in decoded_base64_authorization_header:
                return None, None
            contain1 = decoded_base64_authorization_header.split(':', 1)[0]
            contain2 = decoded_base64_authorization_header.split(':', 1)[1]
            return contain1, contain2
