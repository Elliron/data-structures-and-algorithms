class Node:
    # Function to initialize node object
    def __init__(self, value, next = None):
        self.value = value # assigns an address and data to the node
        self.next = next # sets address of next node to none

# Class LinkedList is taking individual Node instances and linking them together in a list
class LinkedList:
    # function to initialize head
    def __init__(self, node = None):
        self.head = node

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return self

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append_to_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert_before(self, target, value):
        node = self.head
        while node.next is not None:
            if target == node.next.value:
                break
            node = node.next
        if node == None:
            print("No Value")
        else:
            new_node = Node(value)
            new_node = node.next
            node.next = new_node

    def insert_after(self, target, value):
        node = self.head
        while node.next is not None:
            if target == node.value:
                break

            node = node.next
        if node == None:
            print("No Value")
        else:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

# code execution
if __name__ =='__main__':

    # Starts with the empty list
    llist = LinkedList()
    llist.insert("apple").insert("banana").insert("orange").insert("pear")
    entire_list = str(llist)
    print(entire_list)


