from code_challenges.stack_queue_animal_shelter import AnimalShelter, Node
import pytest

def test_one():
    node = Node('apples', None)
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None

def test_shelter():
    queue = AnimalShelter()
    node1 = Node("dog")
    node2 = Node("dog")
    node3 = Node("cat")
    node4 = Node("dog")
    queue.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    actual = queue.__str__()
    expected = "{'dog'} ->{'dog'} ->{'cat'} ->{'dog'} -> None "
    assert actual == expected

def test_queue_enqueue_one():
    queue = AnimalShelter()
    node1 = Node("dog")
    node2 = Node("dog")
    node3 = Node("cat")
    node4 = Node("dog")
    queue.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    queue.enqueue("cat")
    actual = queue.front.value
    expected = "cat"
    assert actual == expected

def test_enqueue_multiple():
    queue = AnimalShelter()
    node1 = Node("dog")
    node2 = Node("dog")
    node3 = Node("cat")
    node4 = Node("dog")
    queue.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    queue.enqueue("cat")
    queue.enqueue("dog")
    actual = queue.__str__()
    expected = "{'cat'} ->{'dog'} -> None "
    assert actual == expected

def test_enqueue_multiple_not():
    queue = AnimalShelter()
    node1 = Node("dog")
    node2 = Node("dog")
    node3 = Node("cat")
    node4 = Node("dog")
    queue.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    queue.enqueue("cat")
    queue.enqueue("dog")
    actual = queue.__str__()
    expected = "{'dog'} ->{'cat'} -> None "
    assert actual != expected

def test_dequeue():
    queue = AnimalShelter()
    node1 = Node("dog")
    node2 = Node("dog")
    node3 = Node("cat")
    node4 = Node("dog")
    queue.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    queue.dequeue("cat")
    actual = queue.__str__()
    expected = "{'dog'} ->{'cat'} ->{'dog'} -> None "
    assert actual == expected

def test_dequeue_multiple():
    queue = AnimalShelter()
    node1 = Node("dog")
    node2 = Node("dog")
    node3 = Node("cat")
    node4 = Node("dog")
    queue.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    queue.dequeue("cat")
    actual = queue.__str__()
    expected = "{'cat'} ->{'dog'} -> None "
    assert actual == expected



