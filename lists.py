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


"""
TASK-1: Write a function that retrieves an element from a list like in C.
    -Prototype: def element_at(my_list, idx):
    -If idx is negative, the function should return None
    -If idx is out of range (> of number of element in my_list), the function should return None
    -You are not allowed to import any module
    -You are not allowed to use try/except
"""


def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0 or idx > n - 1:
        return None
    else:
        return my_list[idx]


"""
TASK-2: Write a function that replaces an element of a list at a specific position (like in C).
    - Prototype: def replace_in_list(my_list, idx, element):
    - If idx is negative, the function should not modify anything, and returns the original list
    - If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
    - You are not allowed to import any module
    - You are not allowed to use try/except
"""


def replace_in_list(my_list, idx, new_element):
    n = len(my_list)
    if idx < 0 or idx > n - 1:
        return my_list
    else:
        my_list[idx] = new_element
        return my_list


"""
Task-3 : Write a function that prints all integers of a list, in reverse order.
    -Prototype: def print_reversed_list_integer(my_list=[]):
    -Format: one integer per line. See example
    -You are not allowed to import any module
    -You can assume that the list only contains integers
    -You are not allowed to cast integers into strings
    -You have to use str.format() to print integers
"""


def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    for index in range(0, n):
        print("{}".format(my_list[(n - 1) - index]))


"""
Task-4 : Write a function that replaces an element in a list at a specific position without modifying the original list
    -Prototype: def new_in_list(my_list, idx, element):
    -If idx is negative, the function should return a copy of the original list
    -If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
    -You are not allowed to import any module
    -You are not allowed to use try/except
"""


def new_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0 or idx > n - 1:
        return my_list
    else:
        new_list = my_list[:n]
        new_list[idx] = element
        return new_list
