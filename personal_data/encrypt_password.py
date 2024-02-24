#!/usr/bin/env python3
"""Encrypting passwords"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Expect one string argument and returns a byte string.
    Expect one string argument and returns a byte string.
    """

    salt = bcrypt.gensalt()
    pw_encoded = password.encode()
    return bcrypt.hashpw(pw_encoded, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password matches the hashed password
    """"
    pw_encoded = password.encode()
    return bcrypt.checkpw(pw_encoded, hashed_password)