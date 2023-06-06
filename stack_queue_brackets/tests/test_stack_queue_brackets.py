import pytest
from stack_queue_brackets.stackqueuebrackets.stack_queue_brackets import (
  validate_brackets
)


def test_1():
    actual = validate_brackets("{}") #call the function with the test value
    expected = True #put the expected result 
    assert actual == expected  #it will return true or false 

def test_2():
    actual = validate_brackets("{}(){}") #call the function with the test value
    expected = True #put the expected result 
    assert actual == expected  #it will return true or false 

def test_3():
    actual = validate_brackets("()[[Extra Characters]]") #call the function with the test value
    expected = True #put the expected result 
    assert actual == expected  #it will return true or false 

def test_4():
    actual = validate_brackets("(){}[[]]") #call the function with the test value
    expected = True #put the expected result 
    assert actual == expected  #it will return true or false 

def test_5():
    actual = validate_brackets("{}{Code}[Fellows](())") #call the function with the test value
    expected = True #put the expected result 
    assert actual == expected  #it will return true or false 

def test_6():
    actual = (validate_brackets("[({}]")) #call the function with the test value
    expected = False #put the expected result 
    assert actual == expected  #it will return true or false 

def test_7():
    actual = validate_brackets("(](") #call the function with the test value
    expected = False #put the expected result 
    assert actual == expected  #it will return true or false 

def test_8():
    actual = validate_brackets("{(})") #call the function with the test value
    expected = False #put the expected result 
    assert actual == expected  #it will return true or false 

def test_9():
    actual = validate_brackets("{]") #call the function with the test value
    expected = (False, 'error closing ]. Doesn’t match opening {.') #put the expected result 
    assert actual == expected  #it will return true or false 

def test_10():
    actual = validate_brackets("[({})]") #call the function with the test value
    expected = True #put the expected result 
    assert actual == expected  #it will return true or false 

def test_11():
    actual = validate_brackets("{") #call the function with the test value
    expected = (False, 'error unmatched opening { remaining.') #put the expected result 
    assert actual == expected  #it will return true or false 

def test_12():
    actual = validate_brackets(")")#call the function with the test value
    expected = (False, 'error closing ) arrived without corresponding opening') #put the expected result 
    assert actual == expected  #it will return true or false 

