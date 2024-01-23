#!/usr/bin/env python3
"""function to find list of schools with certain
topic"""


def schools_by_topic(mongo_collection, topic):
    """return a list of schools with this topic"""
    schools = mongo_collection.find({"topics": topic})
    return schools
