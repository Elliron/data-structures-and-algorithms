class EmpyError(Exception):
    pass

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, top=None):
        self.top = top

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception('Empty')
        result = self.top.value
        self.top = self.top.next
        return result

    def peek(self):
            if self.is_empty():
                raise Exception('Empty')
            return self.top.value

    def __str__(self):
        string = ""
        current = self.top
        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next
        string += f" None "
        return string

def stack_brackets(string):
    stk = Stack()
    for char in string:
        if char in ["(", "{", "["]:
            stk.push(char)
        else:
            if not stk:
                return False
            current_char = stk.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
            if current_char == '{':
                if char != "}":
                    return False

    if stk:
        return False
    return True




# if __name__ == "__main__":
