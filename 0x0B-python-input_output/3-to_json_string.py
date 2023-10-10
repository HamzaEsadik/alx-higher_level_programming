#!/usr/bin/python3
"""method append_write"""


def append_write(filename="", text=""):
    """
    function that returns an object
    represented by a JSON string
    """
    with open(filename, mode="a", encoding="utf-8") as my_file_4:
        return my_file_4.write(text)
