
class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return self.size == 0
        else:
            return self.size

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        result = self.top.value
        self.top = self.top.next
        self.size -= 1
        return result

    def peek(self):
        if self.is_empty():
            raise Exception('empty stack')
        return self.top.value

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
        # elif(self.front == None):
        #     self.back = None

    def peek(self):
        self.is_empty()
        return self.front.next.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

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
