#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    once = 0
    for i in range(x):
        try:

            if my_list[i] / 2 == 0:
                once += 1
                print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
    print()
    return once
