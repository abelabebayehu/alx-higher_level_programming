#!/usr/bin/python3
def lookup(obj):
    """Looks up object's attributes/methods
    Args:
        obj
    Returns the list of available attributes and methods of an object
    """

    return dir(obj)
