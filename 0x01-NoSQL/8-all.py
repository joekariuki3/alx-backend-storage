#!/usr/bin/env python3
"""script that lists all documents in a collection"""


def list_all(mongo_collection):
    """return a list od objects or empty list"""
    documents = [document for document in mongo_collection.find()]
    if not documents:
        return []
    return documents
