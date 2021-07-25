from linked_list.linked_list import Node
from code_challenges.stack_queue.stack_and_queue import Node, Stack, Queue
import pytest

def test_node_one():
    node = Node('apples', None)
    actual = node.value.__str__()
    expected = 'apples'
    assert actual == expected

def test_node_two():
    node = Node('apples', None)
    actual = node.value.__str__()
    expected = 'pear'
    assert actual != expected

def test_stack_push_one():
    stk = Stack()
    node1 = Node("T")
    node2 = Node("h")
    node3 = Node("is")
    node4 = Node("s")
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    stk.push("one")
    actual = stk.__str__()
    expected = "{'one'} ->{'T'} ->{'h'} ->{'is'} ->{'s'} -> None "
    assert actual == expected

def test_stack__push_two():
    stk = Stack()
    node1 = Node("T")
    node2 = Node("h")
    node3 = Node("is")
    node4 = Node("s")
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    stk.push("one")
    actual = stk.__str__()
    expected = "{'WRONG'} ->{'T'} ->{'h'} ->{'is'} ->{'s'} -> None "
    assert actual != expected

def test_stack_push_three():
    stk = Stack()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    stk.push(5)
    stk.push(6)
    actual = stk.__str__()
    expected = "{6} ->{5} ->{4} ->{3} ->{2} ->{1} -> None "
    assert actual == expected

def test_stack_pop_one():
    stk = Stack()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    stk.pop()
    actual = stk.__str__()
    expected = "{3} ->{2} ->{1} -> None "
    assert actual == expected

def test_stack_pop_two():
    stk = Stack()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    stk.pop()
    actual = stk.__str__()
    expected = "{1} ->{3} ->{2} -> None "
    assert actual != expected

def test_stack_pop_three():
    stk = Stack()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    stk.pop()
    stk.pop()
    actual = stk.__str__()
    expected = "{2} ->{1} -> None "
    assert actual == expected

def test_stack_peek_one():
    stk = Stack()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    actual = stk.peek()
    expected = 5
    assert actual == expected

def test_stack_peek_two():
    stk = Stack()
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    stk.top = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    actual = stk.peek()
    expected = "{8}"
    assert actual != expected

def test_queue_enqueue_one():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(8)
    queue.enqueue(1)
    expected ="{5} ->{8} ->{1} -> None "
    actual = queue.__str__()
    assert actual == expected

def test_queue_enqueue_two():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(8)
    queue.enqueue(1)
    queue.enqueue(6)
    expected = "{5} ->{8} ->{1} ->{6} -> None "
    actual = queue.__str__()
    assert actual == expected

def test_queue_dequeue_one():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(8)
    queue.enqueue(1)
    queue.enqueue(6)
    queue.dequeue()
    expected = 5
    actual = queue.front.value
    assert actual != expected

def test_queue_dequeue_one():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.dequeue()
    actual = queue.__str__()
    expected = "{1} ->{3} ->{2} -> None "
    assert actual != expected

def test_queue_peek_one():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.peek()
    actual = queue.__str__()
    expected = "{5}"
    assert actual == expected

def test_queue_peek_two():
    queue = Queue(Node(5, Node(1, Node(2, Node(3)))))
    queue.peek()
    actual = queue.__str__()
    expected = "{5}"
    assert actual != expected

# def test_queue_peek_three():
#     queue = Queue()
#     queue.peek()
#     actual = "empty queue"
#     expected = "empty queue"
#     assert actual == expected
