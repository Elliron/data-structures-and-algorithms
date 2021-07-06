class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, node = None):
        self.top = node

    def is_emptyy(self):
        if self.top is None:
            raise Exception("empty stack")

    def push(self, value):
        node = Node(value)
        node.next = self.top.next
        self.top.next = node

    def pop(self):
        self.is_emptyy()
        popped = self.top.value
        self.top = self.top.next
        return popped

    def peek(self):
        self.is_emptyy()
        return self.top.next.value

    def __str__(self):
        string = ""
        current = self.top.next
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

class Queue:
    def __init__(self, node = None):
        self.front = self.back = node

    def __str__(self):
        string = ""
        current = self.front.next
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

    def enqueue(self, value):
        temp = Node(value)

        if self.back == None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp

    def dequeue(self):
        self.is_empty()
        temps = self.front
        self.front = temps.next
        if(self.front == None):
            self.back = None

    def peek(self):
        self.is_empty()
        return self.front.next.value

    def is_empty(self):
        if self.front is None:
            raise Exception("empty queue")

if __name__ =='__main__':

    stk = Stack()
    stk.push("apple")
    stk.push("pear")
    stk.push("kiwi")
    stk.push("watermelon")
    entire_list = str(stk)
    print(entire_list)

    queue = Queue()
    queue.enqueue("huh")
    queue.enqueue("my")
    queue.enqueue("name")
    queue.enqueue("is")
    entire_queue = str(queue)
    print(entire_queue)
