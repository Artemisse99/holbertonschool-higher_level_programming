#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number <= 0:
            mod = number % -10
else:
            mod = number % 10

line = "Last digit of"
if mod != 0:
        if mod > 5:
                    print("{} {:d} is {:d} and is greater than 5".format( line, number, mod))
        elif mod < 6:
                    print("{} {:d} is {:d} and is less than 6 and not 0".format( line, number, mod))
else:
        print("{} {:d} is {:d} and is 0".format(line, number, mod))
