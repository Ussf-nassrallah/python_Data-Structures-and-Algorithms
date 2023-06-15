from set_dictionary import *

# Task: 0
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)

# Task: 1
# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)
#
# print(new_list)
# print(my_list)

# Task-2
# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))

# Task-3
# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# c_set = common_elements(set_1, set_2)
# print(sorted(list(c_set)))

# Task-4
# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# od_set = only_diff_elements(set_1, set_2)
# print(sorted(list(od_set)))

# Task-5
# a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
# nb_keys = number_keys(a_dictionary)
# print("Number of keys: {:d}".format(nb_keys))

# Task-6
# a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
# print_sorted_dictionary(a_dictionary)

# Task-7
# a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
# new_dict = update_dictionary(a_dictionary, 'language', "Python")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)
#
# print("--")
# print("--")
#
# new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)

# Task-8
# a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
# new_dict = simple_delete(a_dictionary, 'track')
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)
#
# print("--")
# print("--")
# new_dict = simple_delete(a_dictionary, 'c_is_fun')
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

# Task-9
# a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
# new_dict = multiply_by_2(a_dictionary)
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

# Task-10
# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))
#
# best_key = best_score(None)
# print("Best score: {}".format(best_key))

# Task-11
# my_list = [1, 2, 3, 4, 6]
# new_list = multiply_list_map(my_list, 4)
# print(new_list)
# print(my_list)

# advanced task
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))