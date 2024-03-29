#!/usr/bin/env python3
"""
Function that inserts a new document
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection based on kwargs
    """

    id_doc = mongo_collection.insert(kwargs)
    return id_doc
