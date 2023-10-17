#!/usr/bin/env python3
""" Python function that changes all topics in a mongo document """


def update_topics(mongo_collection, name, topics):
    """
    updates all topics
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
