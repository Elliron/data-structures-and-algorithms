
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

# https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/
# https://www.geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/
    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def getpos( self, count, k = 2):
        this_one = count - k
        for this_one in LinkedList:
            return return this_one



# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print("ya", llist.getpos())
    print ("Count of nodes is :",llist.getCount())
