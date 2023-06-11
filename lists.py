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
        print("{:d}".format(my_list[index]))


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
    if isinstance(my_list, list):
        n = len(my_list)
        for index in range(0, n):
            print("{:d}".format(my_list[(n - 1) - index]))


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

"""
Task-5 - Write a function that removes all characters c and C from a string.
    -Prototype: def no_c(my_string):
    -The function should return the new string
    -You are not allowed to import any module
    -You are not allowed to use str.replace()
"""


def no_c(my_string):
    str_len = len(my_string)
    new_string = ""
    for index in range(0, str_len):
        if my_string[index] != 'c' and my_string[index] != 'C':
            new_string += my_string[index]
    return new_string


"""
Task-6: Write a function that prints a matrix of integers.
    -Prototype: def print_matrix_integer(matrix=[[]]):
    -Format: see example
    -You are not allowed to import any module
    -You can assume that the list only contains integers
    -You are not allowed to cast integers into strings
    -You have to use str.format() to print integers
"""


def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        for ele in inner_list:
            if ele == inner_list[-1]:
                print("{:d}".format(ele), end="")
            else:
                print("{:d}".format(ele), end=" ")
        print()


"""
Task-7: Write a function that adds 2 tuples.
    -Prototype: def add_tuple(tuple_a=(), tuple_b=()):
    -Returns a tuple with 2 integers:
    -The first element should be the addition of the first element of each argument
    -The second element should be the addition of the second element of each argument
    -You are not allowed to import any module
    -You can assume that the two tuples will only contain integers
    -If a tuple is smaller than 2, use the value 0 for each missing integer
    -If a tuple is bigger than 2, use only the first 2 integers
"""


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)[:2 - len(tuple_a)]
    tuple_b += (0, 0)[:2 - len(tuple_b)]

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new_tuple = (a, b)

    return new_tuple


"""
Task-8: Write a function that returns a tuple with the length of a string and its first character.
    -Prototype: def multiple_returns(sentence):
    -If the sentence is empty, the first character should be equal to None
    -You are not allowed to import any module
"""


def multiple_returns(sentence):
    n = len(sentence)
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    return (n, first_char)


"""
Task-9: Write a function that finds the biggest integer of a list.
    -Prototype: def max_integer(my_list=[]):
    -If the list is empty, return None
    -You can assume that the list only contains integers
    -You are not allowed to import any module
    -You are not allowed to use the builtin max()
"""


def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        n = len(my_list)
        my_list.sort()
        return my_list[n - 1]


"""
Task-10: Write a function that finds all multiples of 2 in a list.
    -Prototype: def divisible_by_2(my_list=[]):
    -Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
    -The new list should have the same size as the original list
    -You are not allowed to import any module
"""


def divisible_by_2(my_list=[]):
    n = len(my_list)
    output = []
    for index in range(0, n):
        if my_list[index] % 2 == 0:
            output.append(True)
        else:
            output.append(False)
    return output
