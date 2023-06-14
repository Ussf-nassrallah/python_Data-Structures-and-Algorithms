"""
Task-0: Write a function that computes the square value of all integers of a matrix.
    -Prototype: def square_matrix_simple(matrix=[]):
    -matrix is a 2 dimensional array
    -Returns a new matrix:
    -Same size as matrix
    -Each value should be the square of the value of the input
    -Initial matrix should not be modified
    -You are not allowed to import any module
    -You are allowed to use regular loops, map, etc.
"""


def square_matrix_simple(matrix=[]):
    n = len(matrix)
    new_list = matrix.copy()
    for index in range(0, n):
        new_list[index] = list(map(lambda x: x**2, new_list[index]))
    return new_list


"""
Task:1 - Write a function that replaces all occurrences of an element by another in a new list.
    -Prototype: def search_replace(my_list, search, replace):
    -my_list is the initial list
    -search is the element to replace in the list
    -replace is the new element
    -You are not allowed to import any module
"""


def search_replace(my_list, search, replace):
    n = len(my_list)
    new_list = my_list.copy()
    for index in range(0, n):
        if new_list[index] == search:
            new_list[index] = replace
    return new_list


"""
Task:2 - Write a function that adds all unique integers in a list (only once for each integer).
    -Prototype: def uniq_add(my_list=[]):
    -You are not allowed to import any module
"""


def uniq_add(my_list=[]):
    new_list = set(my_list)
    output = 0
    for num in new_list:
        output += num
    return output


"""
Task:3 - Write a function that returns a set of common elements in two sets.
    -Prototype: def common_elements(set_1, set_2):
    -You are not allowed to import any module
"""


def common_elements(set_1, set_2):
    results = set_1 & set_2
    return results


"""
Task:4 - Write a function that returns a set of all elements present in only one set.
    -Prototype: def only_diff_elements(set_1, set_2):
    -You are not allowed to import any module
"""


def only_diff_elements(set_1, set_2):
    results = set_1 ^ set_2
    return results


"""
Task:5 - Write a function that returns the number of keys in a dictionary.
    - Prototype: def number_keys(a_dictionary):
    - You are not allowed to import any module
"""


def number_keys(a_dictionary):
    output = a_dictionary.keys()
    n = len(output)
    return n


"""
Task:6 - Write a function that prints a dictionary by ordered keys.
    -Prototype: def print_sorted_dictionary(a_dictionary):
    -You can assume that all keys are strings
    -Keys should be sorted by alphabetic order
    -Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
    -Dictionary values can have any type
    -You are not allowed to import any module
"""


def print_sorted_dictionary(a_dictionary):
    dictionary_keys = a_dictionary.keys()
    sorted_di_keys = sorted(dictionary_keys)
    for ele in sorted_di_keys:
        print("{}: {}".format(ele, a_dictionary[ele]))


"""
Task-7: Write a function that replaces or adds key/value in a dictionary.
    -Prototype: def update_dictionary(a_dictionary, key, value):
    -key argument will be always a string
    -value argument will be any type
    -If a key exists in the dictionary, the value will be replaced
    -If a key doesn’t exist in the dictionary, it will be created
    -You are not allowed to import any module
"""


def update_dictionary(a_dictionary, key, value):
    dictionary_keys = a_dictionary.keys()
    if key in dictionary_keys:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary


"""
Task-8: Write a function that deletes a key in a dictionary.
    -Prototype: def simple_delete(a_dictionary, key=""):
    -key argument will be always a string
    -If a key doesn’t exist, the dictionary won’t change
    -You are not allowed to import any module
"""


def simple_delete(a_dictionary, key=""):
    dictionary_keys = a_dictionary.keys()
    if key in dictionary_keys:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary


"""
Task-9: Write a function that returns a new dictionary with all values multiplied by 2
    -Prototype: def multiply_by_2(a_dictionary):
    -You can assume that all values are only integers
    -Returns a new dictionary
    -You are not allowed to import any module`
"""


def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    new_dictionary_keys = list(new_dictionary.keys())
    for ele in new_dictionary_keys:
        new_dictionary[ele] = new_dictionary[ele] * 2
    return new_dictionary


"""
Task-10: Write a function that returns a key with the biggest integer value.
    -Prototype: def best_score(a_dictionary):
    -You can assume that all values are only integers
    -If no score found, return None
    -You can assume all students have a different score
    -You are not allowed to import any module
"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        output = max(a_dictionary, key=a_dictionary.get)
        return output


"""
Task:12 - Write a function that returns a list with all values multiplied by a number without using any loops.
    - Prototype: def multiply_list_map(my_list=[], number=0):
    - Returns a new list:
    - Same length as my_list
    - Each value should be multiplied by number
    - Initial list should not be modified
    - You are not allowed to import any module
    - You have to use map
    - Your file should be max 3 lines
"""


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda num: num*number, my_list.copy()))


"""
Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first
    Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

    You can assume the number will be between 1 to 3999.
    def roman_to_int(roman_string) must return an integer
    If the roman_string is not a string or None, return 0
"""


def roman_to_int(roman_string):
    if not (type(roman_string) == str) or roman_string is None:
        return 0
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    output, old = 0, 0
    for c in reversed(roman_string):
        value = values.get(c, 0)
        if value >= old:
            output += value
        else:
            output -= value
        old = value
    return output


"""
Write a function that returns the weighted average of all integers tuple (<score>, <weight>)
    -Prototype: def weight_average(my_list=[]):
    -Returns 0 if the list is empty
    -You are not allowed to import any module
"""


def weight_average(my_list=[]):
    """OPERATION"""
    """input = [(1, 2), (2, 1), (3, 10), (4, 2)]"""
    """left_operation = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2))"""
    """right_operation = (2 + 1 + 10 + 2)"""
    """output = left_operation / right_operation"""

    """LOGIC"""
    left_operation, right_operation, output = 0, 0, 0
    n = len(my_list)
    if not my_list:
        return output
    else:
        for index in range(0, n):
            left_operation += my_list[index][0] * my_list[index][1]
            right_operation += my_list[index][1]
        output = left_operation / right_operation
        return output