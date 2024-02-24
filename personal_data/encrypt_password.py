#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Expect one string argument and returns a byte string.
    """
    pw_encoded = password.encode('utf-8')
    return bcrypt.hashpw(pw_encoded, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password matches the hashed password
    """"
    pw_encoded = password.encode('utf-8')
    return bcrypt.checkpw(pw_encoded, hashed_password)
