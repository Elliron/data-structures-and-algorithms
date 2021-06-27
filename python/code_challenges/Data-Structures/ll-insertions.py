# Class Node creates single instances of a Node Object

class Node:
    # Function to initialize node object
    def __init__(self, data):
        self.data = data # assigns an address and data to the node
        self.next = None # sets address of next node to none

# Class LinkedList is taking individual Node instances and linking them together in a list
class LinkedList:
    # function to initialize head
    def __init__(self):
        self.head = None

        # function to print list from head to end
    def printlist(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

        # function to append to the end of the list
    def append_to_end(self, new_data):
        # Create new node, insert data, set next as none
        new_node = Node(new_data)
        # if empty make new node head of list
        if self.head is None:
            self.head = new_node
            return
        # else traverse till the last node in list
        last = self.head
        while (last.next):
            last = last.next
        # change the next of last node
        last.next = new_node

        # insert a new node after a specified node
    def insert_new_node_after(self, previous_node, new_data):
        # chest if previous node exists
        if previous_node is None:
            print("node does not exist")
            return
        # create new node and put in data
        new_node = Node(new_data)
        # change next of new Node to next of previous_node
        new_node.next = previous_node.next
        # change next of the previous_node to new_node
        previous_node.next = new_node

        # insert a new node before a specified node
    def insert_new_node_before(self, next_node, new_data):
        # check if next_node exists
        if next_node is None:
            print("node does not exist")
            return
        # create new node and put in data
        new_node = Node(new_data)
        # find the node whose next is = to next_node and replace it with the new nodes new_data
        if self.head.new_data is next_node:
            self.head.next = new_data
        # change next of new node to next_node
        new_node.next = next_node

                # code execution
if __name__ =='__main__':

    # Starts with the empty list
    llist = LinkedList()
    llist.append_to_end(5)
    llist.append_to_end(8)
    llist.append_to_end(6)
    # llist.insert_new_node_before(llist.)
    # llist.insert_new_node_after(8, 4)

    llist.printlist()


        # print_LinkedList verifies if the head or first Node in the list exists, if not it is empty and it will print "Linked List is Empty" otherwise it prints the list
    # def print_LinkedList(self):
    #     printvalue = self.head
    #     while printvalue is not None:
    #         print (printvalue.data)
    #         printvalue = printvalue.next

        # add_end addes a new node to the end of the linked list, it traverses the list and changes the nexterence value of the final node to the address of the new node being added.  The new node being added nexterences an address of None
    # def add_end(self, data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         n = self.head
    #         while n.next is not None:
    #             n = n.next
    #         n .next = new_node

    # add_before adds a new node before a specific node in the list, it traverses the list and finds a specific node in the list. It then finds its previous node in the list.  In the previous node it changes the address for its next from the specific nodes value to the value of the new node.  The new nodes address of its next becomes the value of the original specified node.
    # def add_before(self, data):
    #     if self.head is None:
    #         print("Empty List")
    #         return
    #     if self.head.data == x:
    #         new_node = Node(data)
    #         new_node.next = self.head
    #         self.head = new_node
    #         return
    #     n = self.head
    #     while n.next is not None:
    #         if n.next.data == x:
    #             break
    #             n = n.next
    #         if n.next is None:
    #             print("Node not found")
    #         else:
    #             new_node = Node(data)
    #             new_node.next = n.next
    #             n.next = new_node

    # def add_before(self, midde_node, new_data):
    #     if midde_node is None:
    #         print("Node missing")
    #         return

    #     NewNode = Node(new_data)
    #     NewNode.next = middle_node.next
    #     middle_node.next = NewNode

    # # add_after addes a new node after a specific node in the list.  it traverses the list until it finds a node with a specific value.  It then changes the address of its next node to the new nodes value while the new node changes its address of next to the value it had replaced.
    # def add_after(self, data, x):
    #     n = self.head
    #     while n is not None:
    #         if x == n.data:
    #             break
    #         n = n.next
    #     if n is None:
    #         print("node is not present in linked list")
    #     else:
    #         new_node = Node(data)
    #         new_node.next = n.next
    #         n.next = new_node

    # LL1 = LinkedList()
    # LL1.add_end(100)



