#!/usr/bin/python3
def read_file(filename=""):
      """
    Reads a text file (UTF8) and prints its content to the standard output.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
