from linked_list.linked_list import LinkedList, Node
from linked_list.linked_list_zip import zip_list
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

def test_eight():
    new_list = LinkedList(Node(1,Node(3,Node(2))))
    new_list.append_to_end(5)
    actual= new_list.__str__()
    expected = "{1} ->{3} ->{2} ->{5} -> None "
    assert actual == expected

def test_nine():
    new_list = LinkedList(Node(1,Node(3,Node(2))))
    new_list.insert_before(3,5)
    actual = "{1} ->{5} ->{3} ->{2} -> None "
    expected = "{1} ->{5} ->{3} ->{2} -> None "
    assert actual == expected

def test_ten():
    new_list = LinkedList(Node(1,Node(3,Node(2))))
    new_list.insert_after(3,5)
    actual = new_list.__str__()
    expected = "{1} ->{3} ->{5} ->{2} -> None "
    assert actual == expected

# Kth from end tests
def test_eleven():
    new_list = LinkedList(Node(1,Node(3,Node(7,Node(2)))))
    expected = 2
    actual = new_list.from_end(0)
    assert actual == expected

def test_twelve():
    new_list = LinkedList(Node(1,Node(3,Node(7,Node(2)))))
    expected = "negative Number"
    actual = new_list.from_end(-1)
    assert actual == expected

def test_thirteen():
    new_list = LinkedList(Node(1,Node(3,Node(7, Node(2)))))
    expected = "Same Length"
    actual = new_list.from_end(4)
    assert actual == expected

def test_fourteen():
    new_list = LinkedList(Node(1,Node(3,Node(7, Node(2)))))
    expected = "Out of Range"
    actual = new_list.from_end(5)
    assert actual == expected

def test_fifteen():
    new_list = LinkedList(Node(1))
    expected = 1
    actual = new_list.from_end(0)
    assert actual == expected

def test_sixteen():
    new_list = LinkedList(Node(1,Node(3,Node(7, Node(2)))))
    expected = 3
    actual = new_list.from_end(2)
    assert actual == expected

# challenge 08
def test_seventeen():
    new_list_one = LinkedList(Node(1,Node(3, Node(5))))
    new_list_two = LinkedList(Node(2,Node(4, Node(6))))
    actual = zip_list(new_list_one, new_list_two)
    expected = '{1} ->{2} ->{3} ->{4} ->{5} ->{6} -> None '
    assert str(actual) == expected

def test_eighteen():
    new_list_one = LinkedList(Node(1,Node(3, Node(5))))
    new_list_two = LinkedList(Node(2,Node(4, Node(6))))
    actual = zip_list(new_list_one, new_list_two)
    expected = '{1} ->{2} ->{3} ->{4} {7} ->{5} ->{6} -> None '
    assert str(actual) != expected


def test_import():
    assert LinkedList
