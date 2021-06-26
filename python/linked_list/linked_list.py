class Node:
    # Function to initialize node object
    def __init__(self, value, next = None):
        self.value = value # assigns an address and data to the node
        self.next = next # sets address of next node to none

# Class LinkedList is taking individual Node instances and linking them together in a list
class LinkedList:
    # function to initialize head
    def __init__(self):
        self.head = None

        # function to print list from head to end
    # def to_string(self):
    #     temp = self.head
    #     while (temp):
    #         print (temp.data)
    #         temp = temp.next

    def insert(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self

# https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
    def includes(self, search_key):
        current = self.head
        while current != None:
            if current.data == search_key:
                return True

            current = current.next

        return False

    def __str__(self):
        string = ""
        current = self.head
        while current is None:
            string += f"{ {current.value} } ->"
            current = current.next

        string += f" None "

        return string

        # function to append to the end of the list
    # def append_to_end(self, new_data):
    #     # Create new node, insert data, set next as none
    #     new_node = Node(new_data)
    #     # if empty make new node head of list
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     # else traverse till the last node in list
    #     last = self.head
    #     while (last.next):
    #         last = last.next
    #     # change the next of last node
    #     last.next = new_node

    #     # insert a new node after a specified node
    # def insert_new_node_after(self, previous_node, new_data):
    #     # chest if previous node exists
    #     if previous_node is None:
    #         print("node does not exist")
    #         return
    #     # create new node and put in data
    #     new_node = Node(new_data)
    #     # change next of new Node to next of previous_node
    #     new_node.next = previous_node.next
    #     # change next of the previous_node to new_node
    #     previous_node.next = new_node

        # insert a new node before a specified node
    # def insert_new_node_before(self, next_node, new_data):
    #     # check if next_node exists
    #     if next_node is None:
    #         print("node does not exist")
    #         return
    #     # create new node and put in data
    #     new_node = Node(new_data)
    #     # find the node whose next is = to next_node and replace it with the new nodes new_data
    #     if self.head.new_data is next_node:
    #         self.head.next = new_data
    #     # change next of new node to next_node
    #     new_node.next = next_node

                # code execution
if __name__ =='__main__':

    # Starts with the empty list
    llist = LinkedList()
    llist.insert("apples")
    entire_list = str(llist)
    print(entire_list)
    # llist.insert_new_node_before(llist.)
    # llist.insert_new_node_after(8, 4)
    print


