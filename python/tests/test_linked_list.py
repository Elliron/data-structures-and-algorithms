from linked_list.linked_list import LinkedList, Node
import pytest

def test_one():
    node = Node('apples', None)
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None

def test_two_not():
    node = Node('apple', None)
    actual = node.value
    expected = 'pear'
    assert actual != expected
    assert node.next == None

def test_three():
    ll2 = LinkedList()
    ll2.insert("banana")
    ll2.insert("orange")
    actual = ll2.head.value
    expected = "orange"
    assert actual == expected

def test_four():
    node1 = Node("apple")
    ll1 = LinkedList(node1)
    actual = ll1.head.value
    expected = "apple"
    assert actual == expected

def test_five():
    ll1 = LinkedList()
    ll1.insert("apple").insert("banana").insert("orange").insert("pear")
    actual = ll1.head.value
    expected = ("pear")
    assert actual == expected

def test_six():
    ll1 = LinkedList()
    ll1.insert("apple").insert("banana").insert("orange").insert("pear")
    actual = ll1.includes("tomato")
    expected = False
    assert actual == expected
def test_seven():
    ll1 = LinkedList()
    ll1.insert("apple").insert("banana").insert("orange").insert("pear")
    actual = str(ll1)
    expected = "{'pear'} ->{'orange'} ->{'banana'} ->{'apple'} -> None "
    assert actual == expected

def test_import():
    assert LinkedList
