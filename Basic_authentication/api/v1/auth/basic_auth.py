#!/usr/bin/env python3
""" Module Basic Authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
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
        if ":" not in decoded_base64_authorization_header:
            return None, None
        contain1 = decoded_base64_authorization_header.split(':', 1)[0]
        contain2 = decoded_base64_authorization_header.split(':', 1)[1]
        return contain1, contain2

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his
        email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user1 in users:
            if user1.is_valid_password(user_pwd):
                return user1

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that overloads Auth and retrieves
        the User instance for a request
        """
        header = self.authorization_header(request)
        if header is None:
            return None

        extract_header = self.extract_base64_authorization_header(header)
        if extract_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(
            extract_header)
        if decoded_header is None:
            return None

        email_suer, pwd_user = self.extract_user_credentials(decoded_header)
        if email_suer is None or pwd_user is None:
            return None
        user = self.user_object_from_credentials(email_suer, pwd_user)
        return user
