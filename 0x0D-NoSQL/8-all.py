#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection
    """

    documents = mongo_collection.find()
    if documents.count() > 0:
        return documents
    return []
