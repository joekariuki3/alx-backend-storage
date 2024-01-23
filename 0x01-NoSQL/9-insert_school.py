#!/usr/bin/env python3
"""script that inserts a new document
in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ insert kwargs in mongo_collection"""
    insertedItem = 0
    for key, value in kwargs.items():
        insertedItem = mongo_collection.insert_one({key: value})
    return insertedItem.inserted_id
