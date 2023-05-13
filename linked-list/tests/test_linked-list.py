import pytest 
from LinkedList.LinkedList import (
  Node , 
  LinkedList
)

def test_empty_linked_list():
    actual = LinkedList() #call the function with the test value
    expected = "LinkedList instance. head = None" #put the expected result 
    assert str(actual) == expected  #it will return true or false 

def test_insert_into_linked_list():
    new_ntst = LinkedList()
    new_ntst.insert(10)
    actual =  new_ntst
    expected = "LinkedList instance. head = Node instance. value = 10 pointer = None"  
    assert str(actual) == expected  

def test_head_point_to_the_first_node():
    new_ntst = LinkedList()
    new_ntst.insert(10)
    new_ntst.insert(11)
    new_ntst.insert(12)
    new_ntst.insert(13)
    actual =  new_ntst
    expected = "LinkedList instance. head = Node instance. value = 13 pointer = Node instance. value = 12 pointer = Node instance. value = 11 pointer = Node instance. value = 10 pointer = None"  
    assert str(actual) == expected  



