
"""
Write a class Node that defines a node of a singly linked list by:

Private instance attribute: data:
property def data(self): to retrieve it
property setter def data(self, value): to set it:
data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
Private instance attribute: next_node:
property def next_node(self): to retrieve it
property setter def next_node(self, value): to set it:
next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
Instantiation with data and next_node: def __init__(self, data, next_node=None):
And, write a class SinglyLinkedList that defines a singly linked list by:

Private instance attribute: head (no setter or getter)
Simple instantiation: def __init__(self):
Should be printable:
print the entire list in stdout
one node number by line
Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
You are not allowed to import any module

"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = Node()

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
