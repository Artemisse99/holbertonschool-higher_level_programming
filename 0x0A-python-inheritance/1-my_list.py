#!/usr/bin/python3

"""
classes
    MyList
"""
class MyList(list):
    """ Class My class """
        def print_sorted(self):
        """
            this function copy list and print sorted values
            Args:
                self: Mylist
        """         
            print(sorted(self))
