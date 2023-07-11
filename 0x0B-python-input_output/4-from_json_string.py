#!/usr/bin/python3
"""Module for load_from_json_file method"""


def from_json_string(my_str):
    """Method for returning an object represented by a JSON string"""
    import json
    return json.loads(my_str)
