#!/usr/bin/python3
a = 97
while a <= 122 :
     if a != 101 and a != 113:
         print("{:c}".format(a), end="")
     a += 1
