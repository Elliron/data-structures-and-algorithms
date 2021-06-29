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

    def from_end(self, k):
        list_head = self.head
        count = 0
        while list_head != None:
            list_head = list_head.next
            count += 1
        if k > count:
            return("Out of Range")
        elif k == count:
            return("Same Length")
        elif k < 0:
            return("negative Number")
        elif k == self:
            return("Linked list needs to be greater than 1")
        list_head = self.head
        for i in range(1,count - k):
            list_head = list_head.next
        return list_head.value

    def zip_list(self, second):
        first_current = self.head
        second_current = second.head
        while first_current is not None and second_current is not None:
            first_current_next = first_current.next
            second_next = second_current.next
            second_current.next = first_current_next
            first_current.next = second_current
            first_current = first_current_next
            second_current = second_next
        second.head = second_current



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


