class Node:
    """
    Class creates an Linked-List
    The object inside has two parameters, itself as the first parameter and the head as the second parameter


    """

    def _init_(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Class creates an empty Linked List
    Define an __init__ method with the parameter head
    Define a method that inserts a new node with a new value into the head of the list.
    Define a method called includes, that uses a boolean to determine if a value exists as a nodes value in the linked list.

Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NONE"
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
    """
    # Linked List Constructor
    def __init__(self, head = None):
        self.head = head

    # Inserts a new node with a new value at the head or start of the linked list.  The value being added cannot be None.
    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node
