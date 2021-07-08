from code_challenges.stack_queue_pseudo.pseudo_queue import Node, Stack, Queue
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
