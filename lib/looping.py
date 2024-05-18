#!/usr/bin/env python3

def happy_new_year():
    i =10
    while (i > 0):
        print(i)
        i -= 1
    else:
        print("Happy New Year!")

def square_integers(int_list):
    int_list = [list ** 2 for list in int_list]
    return int_list


def fizzbuzz():
    for num in range(1, 101):
        if not num % 15:
            print("FizzBuzz")
        elif not num % 5:
            print("Buzz")
        elif not num % 3:
            print("Fizz")
        else:
            print(num)