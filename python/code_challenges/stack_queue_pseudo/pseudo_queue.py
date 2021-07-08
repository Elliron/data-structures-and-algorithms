class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, top = None):
        self.top = top

    def __str__(self):
        string = ""
        current = self.top
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

class Queue:
    def __init__(self, front = None, back = None):
        self.front = front
        self.back = back

    def __str__(self):
        string = ""
        current = self.front
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

    def enqueue(self, value):
        temp = Node(value)
        if self.is_empty():
        # if self.back == None:
            self.front = temp
            self.back = temp
        else:
            self.back.next = temp
            self.back = temp

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        temps = self.front
        self.front = temps.front.next
        return temps.value

    def peek(self):
        self.is_empty()
        return self.front.next.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
