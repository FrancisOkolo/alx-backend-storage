#!/usr/bin/env python3
"""
function to return all mongodb documents
"""

def list_all(mongo_collection):
    '''returns all documents from a collection in a list.
    '''
    return [doc for doc in mongo_collection.find()]
