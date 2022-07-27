#!/usr/bin/env python3
"""
Function that returns the list of school
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of
    school having a specific topic
    """

    list_school = mongo_collection.find({"topics": topic})
    return list_school
