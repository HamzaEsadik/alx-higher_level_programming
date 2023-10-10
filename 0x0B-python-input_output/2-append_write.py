#!/usr/bin/python3
"""read_lines method"""


def read_lines(filename="", nb_lines=0):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, encoding="utf-8") as my_file_0:
        if nb_lines <= 0:
            print(my_file_0.read(), end="")
        else:
            for ln in my_file_0:
                if nb_lines == 0:
                    break
                print(ln, end="")
                nb_lines -= 1
