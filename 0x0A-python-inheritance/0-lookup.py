#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Looks up object's attributes/methods
    Args: obj
    Return a list of an object's available attributes."""
    return (dir(obj))
