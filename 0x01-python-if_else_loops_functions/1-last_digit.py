#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

li = "Last digit of"

if number >= 0:
            m = number % 10
else:
            m = number % -10

if m > 5:
    print("{} {:d} is {:d} and is greater than 5".format(li, number, m))
if m == 0:
    print("{} {:d} is {:d} and is 0".format(li, number, m))
if m < 6 and m != 0:
    print("{} {:d} is {:d} and is less than 6 and not 0".format(li, number, m))
