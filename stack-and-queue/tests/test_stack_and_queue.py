import pytest
from stackAndQueue.stack_and_queue import (
  Node , 
  Stack,
  Queue
)

def test_push_onto_stack():
    test_stack = Stack()
    test_stack.push(1)
    actual = str(test_stack) #call the function with the test value
    expected = "the stack top value = 1" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_push_multiple_values_stack (test_stack_demo):
    actual = str(test_stack_demo) #call the function with the test value
    expected = "the stack top value = 5" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_pop_off_stack(test_stack_demo):
    test_stack_demo.pop()
    actual = str(test_stack_demo) #call the function with the test value
    expected = "the stack top value = 4" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_empty_a_stack_after_multiple_pops(test_stack_demo):
    test_stack_demo.pop()
    test_stack_demo.pop()
    test_stack_demo.pop()
    test_stack_demo.pop()
    test_stack_demo.pop()
    actual = str(test_stack_demo) #call the function with the test value
    expected = "this stack is empty" #put the expected result 
    assert actual == expected  #it will return true or false
    
def test_peek_next_item_on_stack(test_stack_demo):
    test_stack_demo.peek()
    actual = str(test_stack_demo) 
    expected = "the stack top value = 5"  
    assert actual == expected  

def test_instantiate_empty_stack():
    empty_stack = Stack()
    actual = str(empty_stack) 
    expected = "this stack is empty"  
    assert actual == expected  

def test_peek_on_empty_stack():
    empty_stack = Stack()
    with pytest.raises(Exception):
        empty_stack.peek()  

def test_enqueue_into_queue():
    node1 = Node(1)
    queue_test = Queue(node1)
    queue_test.enqueue(Node(2))
    actual = str(queue_test)
    expected = "the queue front = 1,"  
    assert actual == expected 

def test_enqueue_multiple_values_into_queue (test_queue_demo):
    actual = str(test_queue_demo)
    expected = "the queue front = 1,"  
    assert actual == expected 
     
def test_dequeue_out_queue_expected (test_queue_demo):
    test_queue_demo.dequeue()
    actual = str(test_queue_demo)
    expected = "the queue front = 2,"  
    assert actual == expected 

def test_peek_queue (test_queue_demo):
    actual = test_queue_demo.peek()
    expected = "the queue front = 1,"  
    assert actual == expected 

def test_empty_queue_multiple_dequeues (test_queue_demo):
    test_queue_demo.dequeue()
    test_queue_demo.dequeue()
    test_queue_demo.dequeue()
    test_queue_demo.dequeue()
    test_queue_demo.dequeue()
    with pytest.raises(Exception):
        test_queue_demo.dequeue()

def test_instantiate_empty_queue():
    queue_test = Queue()
    actual = str(queue_test)
    expected = "this queue is empty"  
    assert actual == expected 

def test_dequeue_empty_queue_exception():
    queue_test = Queue()
    with pytest.raises(Exception):
        queue_test.dequeue()


def test_peek_empty_queue_exception():
    queue_test = Queue()
    with pytest.raises(Exception):
        queue_test.peek()



#######################
# Fixtures
#######################

@pytest.fixture
def test_stack_demo():
        test_stack = Stack()
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)
        test_stack.push(4)
        test_stack.push(5)
        return test_stack

@pytest.fixture
def test_queue_demo():
    node1 = Node(1)
    test_queue = Queue(node1)
    test_queue.enqueue(Node(2))
    test_queue.enqueue(Node(3))
    test_queue.enqueue(Node(4))    
    test_queue.enqueue(Node(5))
    return test_queue
