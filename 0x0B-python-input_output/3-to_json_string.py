#!/usr/bin/python3
"""Module for to_json_string method"""


def to_json_string(my_obj):
    """Method for returning JSON representation of an object"""
    import json
    return json.dumps(my_obj)
