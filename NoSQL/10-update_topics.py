#!/usr/bin/env python3
""" A Python function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update all topics"""
    mongo_collection.update_Many({"name": name}, {"$set" {"topics": topics}})
