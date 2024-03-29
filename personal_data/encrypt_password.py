#!/usr/bin/env python3
"""
Encrypting passwords
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Expect one string argument and returns a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
