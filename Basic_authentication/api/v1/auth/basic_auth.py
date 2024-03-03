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
