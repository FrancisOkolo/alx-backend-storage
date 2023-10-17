#!/usr/bin/env python3
"""
Python function that returns the list of school
documents having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the matched list
    """
    return mongo_collection.find({"topics": topic})
