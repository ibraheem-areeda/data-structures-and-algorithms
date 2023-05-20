import pytest
from stackAndQueue.stack_and_queue import (
  Node , 
  stack,
  Queue
)

def test_push_onto_stack():
    test_stack = stack()
    test_stack.push(1)
    actual = str(test_stack) #call the function with the test value
    expected = "the stack top value = 1" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_push_multiple_values_stack ():
    test_stack = stack()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    test_stack.push(5)
    actual = str(test_stack) #call the function with the test value
    expected = "the stack top value = 5" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_pop_off_stack():
    test_stack = stack()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    test_stack.push(5)
    test_stack.pop()
    actual = str(test_stack) #call the function with the test value
    expected = "the stack top value = 4" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_empty_a_stack_after_multiple_pops():
    
    


