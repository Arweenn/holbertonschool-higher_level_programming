#!/usr/bin/python3

def fizzbuzz():

    for number in range(1, 100):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=' ')
            continue

        if number % 3 == 0:
            print("Fizz", end=' ')
            continue

        if number % 5 == 0:
            print("Buzz", end=' ')
            continue

        print(f"{number}", end=' ')
