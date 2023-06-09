"""
TASK-0: Write a function that prints all integers of a list.
    - Prototype: def print_list_integer(my_list=[]):
    - Format: one integer per line. See example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use str.format() to print integers
"""

def print_list_integer(my_list=[]):
    n = len(my_list)
    for index in range(0,n):
        print("{}".format(my_list[index]))