from linked_list.linked_list import LinkedList, Node
import pytest

def test_node_constructor_for_object_creation():
    node = Node('apples', None)
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None


def test_import():
    assert LinkedList
