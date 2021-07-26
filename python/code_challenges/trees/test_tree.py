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

def test_tree(empty_tree):
    actual = empty_tree.in_order()
    expected = []
    assert actual == expected

def test_add(fix_tree):
    tree = fix_tree()
    search = BinarySearchTree()
    actual =  fix_tree.in_order()
    expected = 10
    assert actual == expected

@pytest.fixture
def empty_tree():
    empty_tree = BinaryTree()
    return empty_tree

@pytest.fixture
def fix_tree(empty_tree):
    tree = empty_tree()
    tree.root = Node(1)
    tree.root.left = Node(6)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(12)
    tree.root.right = Node(3)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(2)
    return tree

