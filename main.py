from lists import print_list_integer, element_at, replace_in_list

my_list = [1, 2, 3, 4, 5]

# TASK-0
print_list_integer(my_list)

# TASK-1
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

# TASK-2
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
