#!/usr/bin/env python3
"""a class to manage the API authentication."""
from flask import request
from type import List, TypeVar


class Auth():
    """a class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check authentification"""
        if path is None or excluded_paths is None or Not len(excluded_paths):
            return True
        if path[-1] != '\':
            path += '\'
        if excluded_paths[-1] != '\':
            excluded_paths += '\'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """handle authorisation"""
        return False

    def current_user(self, request=None) -> TypeVar('User'):
        """handle current_user"""
        return False
