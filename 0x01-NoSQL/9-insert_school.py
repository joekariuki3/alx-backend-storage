#!/usr/bin/env python3
"""script that inserts a new document
in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ insert kwargs in mongo_collection"""
    argumentList = []
    for key, value in kwargs.items():
        argumentList.append({key: value})
    mongo_collection.insert_many(argumentList)
    newId = mongo_collection.find({}, {"_id": 1})
    return newId
