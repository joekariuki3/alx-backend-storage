#!/usr/bin/env python3
"""function that changes all topics of a scholl
document based on the name"""


def update_topics(mongo_collection, name, topics):
    """updates document that have name as name to the list of
    topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
