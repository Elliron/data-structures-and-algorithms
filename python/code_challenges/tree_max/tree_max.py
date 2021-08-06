from trees.tree import *

def function(BinaryTree):
    queue = Queue()
    max = BinaryTree.root.value.head.value[0]
    queue.enqueue(BinaryTree.root)
    while queue.peek():
        front = queue.dequeue()
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
        current = front.value.head
        while current is not None:
            for number in current.value:
                if number > max:
                    max = number
            current = current.next
    return max
