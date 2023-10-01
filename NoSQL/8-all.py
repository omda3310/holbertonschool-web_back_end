#!/usr/bin/env python3
"""A Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Return lists of all documents in a collection or empty list"""
    if (mongo_collection):
        return list(mongo_collection.find())
    return []
