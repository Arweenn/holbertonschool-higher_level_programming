#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str = "Last digit of"

if number >= 0:
    last = number % 10
else:
    last = number % -10


if last > 5:
    print(f"{str} {number} is {last} and is greater than 5")

if last == 0:
    print(f"{str} {number} is {last} and is 0")

if last < 6 and last != 0:
    print(f"{str} {number} is {last} and is less than 6 and not 0")
