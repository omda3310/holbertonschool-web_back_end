#!/usr/bin/env python3
"""a class to manage the API authentication."""
from flask import request
from type import List, TypeVar


class Auth():
    """a class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check authentification"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        test = path
        if path[-1] != '\':
            test += '\'
        if path in excluded_paths or test in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """handle authorisation"""
        if request is None:
            return False
        return request.headers.get("authorisation")

    def current_user(self, request=None) -> TypeVar('User'):
        """handle current_user"""
        return False
