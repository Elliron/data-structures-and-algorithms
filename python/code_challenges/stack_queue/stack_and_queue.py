
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, value):
        if self.top == None:
            self.top = Node(value)
        else:
            newnode = Node(value)
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        else:
            poppednode = self.top
            self.top = self.top.next
            poppednode.next = None
            return poppednode.value

    def peek(self):
        if self.is_empty():
            raise Exception('empty stack')
        else:
            return self.top.data

    # def __str__(self):
        # string = ""
        # current = self.top
        # while current is not None:
        #     string += f"{ {current.value} } ->"
        #     current = current.next
        # string += f" None "
        # return string

    def display(self):
        iternode = self.top
        if self.isempty():
            print("Stack Underflow")
        else:
            while (iternode != None):

                print(iternode.value, "->",end = " ")
                iternode = iternode.next
            return

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
    # stk.display()
    # entire_list = str(stk)
    # print(entire_list)

    queue = Queue()
    queue.enqueue("huh")
    queue.enqueue("my")
    queue.enqueue("name")
    queue.enqueue("is")
    entire_queue = str(queue)
    print(entire_queue)
