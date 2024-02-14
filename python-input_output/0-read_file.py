#!/usr/bin/python3

def read_file(filename=""):

    with open('my_file_0.txt') as f:
        for line in f:
            print(line, end="")
