import pytest
from stack_queue_pseudo.stack_queue_pseudo import (
  Node , 
  PseudoQueue
)

def test_enqueue_PseudoQueue():
    test_PseudoQueue = PseudoQueue()
    v2 = Node(2)
    v1 = Node(1,Node(v2))
    test_PseudoQueue.enqueue(v1)
    test_PseudoQueue.enqueue(v2)
    actual = str(test_PseudoQueue.stack_in) #call the function with the test value
    expected = "the stack top value = 2 next value = 1" #put the expected result 
    assert actual == expected  #it will return true or fals

def test_multiple_values_enqueue_PseudoQueue():
    test_PseudoQueue = PseudoQueue()
    v6 = Node(6)
    v5 = Node(5,Node(v6))
    v4 = Node(4,Node(v5))
    v3 = Node(3,Node(v4))
    v2 = Node(2,Node(v3))
    v1 = Node(1,Node(v2))
    test_PseudoQueue.enqueue(v1)
    test_PseudoQueue.enqueue(v2)
    test_PseudoQueue.enqueue(v3)
    test_PseudoQueue.enqueue(v4)
    test_PseudoQueue.enqueue(v5)
    test_PseudoQueue.enqueue(v6)
    actual = str(test_PseudoQueue.stack_in) #call the function with the test value
    expected = "the stack top value = 6 next value = 5" #put the expected result 
    assert actual == expected  #it will return true or fals


def test_dequeue_PseudoQueue():
    test_PseudoQueue = PseudoQueue()
    v2 = Node(2)
    v1 = Node(1,Node(v2))
    test_PseudoQueue.enqueue(v1)
    test_PseudoQueue.enqueue(v2)
    test_PseudoQueue.dequeue()
    actual = str(test_PseudoQueue.stack_in) #call the function with the test value
    expected = "the stack top value = 2 next value = None" #put the expected result 
    assert actual == expected  #it will return true or fals

def test_dequeue_multiable_PseudoQueue(test_PseudoQueue_demo):
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    with pytest.raises(Exception):
        test_PseudoQueue_demo.dequeue()

def test_dequeue_multiable_back_PseudoQueue(test_PseudoQueue_demo):
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    test_PseudoQueue_demo.dequeue()
    actual = str(test_PseudoQueue_demo.stack_in) #call the function with the test value
    expected = "the stack top value = 6 next value = None" #put the expected result 
    assert actual == expected  #it will return true or fals

def test_instantiate_empty_PseudoQueue():
    test_PseudoQueue = PseudoQueue()
    actual = str(test_PseudoQueue.stack_in) #call the function with the test value
    expected = "this stack is empty" #put the expected result 
    assert actual == expected  #it will return true or fals

def test_dequeue_empty_PseudoQueue():
    test_PseudoQueue = PseudoQueue()
    with pytest.raises(Exception):
        test_PseudoQueue.dequeue()





#######################
# Fixtures
#######################

@pytest.fixture
def test_PseudoQueue_demo():
    test_PseudoQueue = PseudoQueue()
    v6 = Node(6)
    v5 = Node(5,Node(v6))
    v4 = Node(4,Node(v5))
    v3 = Node(3,Node(v4))
    v2 = Node(2,Node(v3))
    v1 = Node(1,Node(v2))
    test_PseudoQueue.enqueue(v1)
    test_PseudoQueue.enqueue(v2)
    test_PseudoQueue.enqueue(v3)
    test_PseudoQueue.enqueue(v4)
    test_PseudoQueue.enqueue(v5)
    test_PseudoQueue.enqueue(v6)
    return test_PseudoQueue
