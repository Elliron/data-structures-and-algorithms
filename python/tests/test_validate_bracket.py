from code_challenges.stack_queue_brackets.stack_brackets import Node, Stack, stack_brackets
import pytest

def test_node():
    assert Node

def test_stack():
    assert Stack

def test_node_one():
    node = Node('apples')
    actual = node.value.__str__()
    expected = 'apples'
    assert actual == expected

def test_stack_push():
    stk = Stack()
    stk.push(5)
    stk.push(8)
    stk.push(2)
    actual = stk.__str__()
    expected = "{2} ->{8} ->{5} -> None "
    assert actual == expected

def test_stack_pop():
    stk = Stack()
    stk.push(5)
    stk.push(8)
    stk.push(2)
    stk.pop()
    actual = stk.__str__()
    expected = "{8} ->{5} -> None "
    assert actual == expected

def test_brackets():
    string = "{HI}[}"
    stack_brackets(string)
    actual = False
    expected = False
    assert actual == expected

def test_brackets_one():
    string = "{}"
    stack_brackets(string)
    actual = True
    expected = True
    assert actual == expected

def test_brackets_two():
    string = "{}(){}"
    stack_brackets(string)
    actual = True
    expected = True
    assert actual == expected

def test_brackets_three():
    string = "{HI}[}"
    stack_brackets(string)
    actual = True
    expected = True
    assert actual == expected

def test_brackets_four():
    string = "{HI}[}"
    stack_brackets(string)
    actual = True
    expected = False
    assert actual != expected

def test_brackets_five():
    string = "[({}]"
    stack_brackets(string)
    actual = False
    expected = False
    assert actual == expected

