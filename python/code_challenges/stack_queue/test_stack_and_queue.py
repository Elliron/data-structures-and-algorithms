# from stack_and_queue import *
# import pytest


# def test_node():
#     node = Node("apple")
#     assert node.value == "apple"

# # ----------------------Stack-------------------------
# def test_push(fixed_stack):
#     fixed_stack.push(1)
#     actual = fixed_stack.top.value
#     expected = 1
#     assert actual == expected

# def test_push_not(fixed_stack):
#     fixed_stack.push(1)
#     actual = fixed_stack.top.value
#     expected = 50
#     assert actual != expected


# def test_push_multiple(empty_stack):
#     empty_stack.push(1)
#     empty_stack.push(6)
#     empty_stack.push(9)
#     actual = empty_stack.__str__()
#     expected = '{9} ->{6} ->{1} -> None '
#     assert actual == expected

# def test_push_multiple_not(empty_stack):
#     empty_stack.push(10)
#     empty_stack.push(16)
#     empty_stack.push(99)
#     actual = empty_stack.__str__()
#     expected = '{9} ->{6} ->{1} -> None '
#     assert actual != expected

# def test_pop(fixed_stack):
#     actual = fixed_stack.pop()
#     expected = 9
#     assert actual == expected

# def test_pop_not(fixed_stack):
#     actual = fixed_stack.pop()
#     expected = 20
#     assert actual != expected

# def test_pop_till_empty(fixed_stack):
#     fixed_stack.pop()
#     fixed_stack.pop()
#     fixed_stack.pop()
#     actual = fixed_stack.__str__()
#     expected =' None '
#     assert actual == expected

# def test_peek(fixed_stack):
#     actual = fixed_stack.peek()
#     expected = 9
#     assert actual == expected

# def test_peek_not(fixed_stack):
#     actual = fixed_stack.peek()
#     expected = 25
#     assert actual != expected

# def test_exception_pop(empty_stack):
#     with pytest.raises(CustomError) as e:
#         empty_stack.pop()
#         assert str(e.value) == "Empty Stack"

# def test_exception_peek(empty_stack):
#     with pytest.raises(CustomError) as e:
#         empty_stack.peek()
#         assert str(e.value) == "Empty Stack"

# # -------------------------Queue-----------------------------#

# def test_enqueue(fixed_queue):
#     fixed_queue.enqueue(1)
#     actual = fixed_queue.back.value
#     expected = 1
#     assert actual == expected

# def test_enqueue_not(fixed_queue):
#     fixed_queue.enqueue(1)
#     actual = fixed_queue.back.value
#     expected = 50
#     assert actual != expected


# def test_enqueue_multiple(empty_queue):
#     empty_queue.enqueue(1)
#     empty_queue.enqueue(6)
#     empty_queue.enqueue(9)
#     actual = 9
#     expected = 9
#     assert actual == expected

# def test_enqueue_multiple_not(empty_queue):
#     empty_queue.enqueue(10)
#     empty_queue.enqueue(16)
#     empty_queue.enqueue(99)
#     actual = empty_queue.__str__()
#     expected = '{24}'
#     assert actual != expected

# def test_dequeue(fixed_queue):
#     actual = fixed_queue.dequeue()
#     expected = 1
#     assert actual == expected

# def test_dequeue_not(fixed_queue):
#     actual = fixed_queue.dequeue()
#     expected = 20
#     assert actual != expected

# def test_dequeue_till_empty(fixed_queue):
#     with pytest.raises(CustomError) as e:
#         fixed_queue.dequeue()
#         fixed_queue.dequeue()
#         fixed_queue.dequeue()
#         fixed_queue.dequeue()
#         assert str(e.value) == "Empty Queue"

# def test_peek(fixed_queue):
#     actual = fixed_queue.peek()
#     expected = 1
#     assert actual == expected

# def test_peek_not(fixed_queue):
#     actual = fixed_queue.peek()
#     expected = 25
#     assert actual != expected

# def test_exception_dequeue(empty_queue):
#     with pytest.raises(CustomError) as e:
#         empty_queue.dequeue()
#         assert str(e.value) == "Empty Queue"

# def test_exception_peek(empty_queue):
#     with pytest.raises(CustomError) as e:
#         empty_queue.peek()
#         assert str(e.value) == "Empty Queue"



# # ------------------------fixtures------------------------
# @pytest.fixture
# def empty_stack():
#     stk = Stack()
#     return stk

# @ pytest.fixture
# def fixed_stack(empty_stack):
#     empty_stack.push(1)
#     empty_stack.push(6)
#     empty_stack.push(9)
#     return empty_stack

# @pytest.fixture
# def empty_queue():
#     queue = Queue()
#     return queue

# @pytest.fixture
# def fixed_queue(empty_queue):
#     empty_queue.enqueue(1)
#     empty_queue.enqueue(6)
#     empty_queue.enqueue(3)
#     return empty_queue
