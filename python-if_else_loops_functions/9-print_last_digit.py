#!/usr/bin/python3

def print_last_digit(number):

    if number >= 0:
        last = number % 10
    else:
        last = number % -10

    return last
