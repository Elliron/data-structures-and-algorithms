from code_challenges.stack_queue.stack_and_queue import Node, Stack, Queue
import pytest

def test_node_one():
    node = Node('apples', None)
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None

def test_node_two():
    node = Node('apples', None)
    actual = node.value
    expected = 'pear'
    assert actual != expected
    assert node.next == None

def test_stack_push_one():
    stk = Stack(Node(1, Node(2, Node(3))))
    stk.push(Node(5))
    actual = stk.__str__()
    expected = "{5} ->{1} ->{2} ->{3} -> None "
    assert actual == expected

def test_stack__push_two():
    stk = Stack(Node(1, Node(2, Node(3))))
    stk.push(Node(5))
    actual = str(stk)
    expected = "{5} ->{1} ->{3} ->{2} -> None "
    assert actual != expected

def test_stack_push_three():
    stk = Stack(Node(1, Node(2, Node(3))))
    stk.push(Node(5))
    stk.push(Node(6))
    actual = str(stk)
    expected = "{6} ->{5} ->{1} ->{3} ->{2} -> None "
    assert actual == expected

def test_stack_pop_one():
    stk = Stack(Node(5, Node(1, Node(2, Node(3)))))
    stk.pop()
    actual = str(stk)
    expected = "{1} ->{3} ->{2} -> None "
    assert actual == expected

def test_stack_pop_two():
    stk = Stack(Node(5, Node(1, Node(2, Node(3)))))
    stk.pop()
    actual = str(stk)
    expected = "{1} ->{3} ->{2} -> None "
    assert actual != expected

def test_stack_pop_three():
    stk = Stack(Node(5, Node(1, Node(2, Node(3)))))
    stk.pop()
    actual = str(stk)
    expected = "{1} ->{3} ->{2} -> None "
    assert actual == expected

def test_stack_peek_one():
    stk = Stack(Node(5, Node(1, Node(2, Node(3)))))
    stk.peek()
    actual = str(stk)
    expected = "{5}"
    assert actual == expected

def test_stack_peek_two():
    stk = Stack(Node(5, Node(1, Node(2, Node(3)))))
    stk.peek()
    actual = str(stk)
    expected = "{8}"
    assert actual != expected

def test_queue_enqueue_one():
    queue = Queue(Node(1, Node(2, Node(3))))
    queue.enqueue(Node(5))
    actual = str(Queue)
    expected = "{5} ->{1} ->{3} ->{2} -> None "
    assert actual == expected

def test_queue_enqueue_two():
    queue = Queue(Node(1, Node(2, Node(3))))
    queue.enqueue(Node(5))
    actual = str(Queue)
    expected = "{1} ->{3} ->{2} -> None "
    assert actual != expected

def test_queue_dequeue_one():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.dequeue()
    actual = str(Queue)
    expected = "{1} ->{3} ->{2} -> None "
    assert actual == expected

def test_queue_dequeue_one():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.dequeue()
    actual = str(Queue)
    expected = "{1} ->{3} ->{2} -> None "
    assert actual != expected

def test_queue_peek_one():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.peek()
    actual = str(Queue)
    expected = "{5}"
    assert actual == expected

def test_queue_peek_two():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.peek()
    actual = str(Queue)
    expected = "{5}"
    assert actual != expected

# def test_queue_peek_three():
#     queue = Queue()
#     queue.peek()
#     actual = "empty queue"
#     expected = "empty queue"
#     assert actual == expected
