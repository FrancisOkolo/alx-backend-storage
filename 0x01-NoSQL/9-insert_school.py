#!/usr/bin/env python3
"""Python function to inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in python using .inserted_id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
