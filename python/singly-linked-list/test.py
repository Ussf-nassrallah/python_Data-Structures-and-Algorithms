from singly_linked_list import *
from challenge import *

# my_list = LinkedList()
#
# my_list.display()
# n1 = my_list.length()
# print(n1)
#
# my_list.append(3)
# my_list.append(1)
# my_list.append(2)
#
# my_list.display()
# n2 = my_list.length()
# print(n2)


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)