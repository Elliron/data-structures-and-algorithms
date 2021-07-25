import pytest
from tree import *

# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


# @pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


# @pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


# @pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


# @pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


# @pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree

def test_node_left(tree):
    actual = tree.root.left.value
    expected =  6
    assert actual == expected

def test_node_left(tree):
    actual = tree.root.left.value
    expected =  9
    assert actual != expected

def test_node_right(tree):
    actual = tree.root.right.value
    expected = 10
    assert actual == expected

def test_node_right(tree):
    actual = tree.root.right.value
    expected = 18
    assert actual != expected

def test_pre_order(tree):
    actual = tree.pre_order()
    expected = 3
    assert actual == expected

def test_in_order(tree):
    pass

def test_post_order(tree):
    pass

def test_add(tree):
    pass

# def test_contains():
#     binary_tree = BinarySearchTree(tree)
#     binary_tree.contains(23)
#     actual = False
#     expected = True
#     assert actual == expected

@pytest.fixture
def empty_tree():
    return empty_tree

@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(6)
    tree.root.right = Node(10)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(12)
    tree.root.right.left = Node(23)
    tree.root.right.right = Node(28)
    return tree

