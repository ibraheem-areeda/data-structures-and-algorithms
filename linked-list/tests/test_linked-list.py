import pytest
from LinkedList.LinkedList import (
  Node , 
  LinkedList
)

def test_numten():
    actual = Node(10) #call the function with the test value
    expected = "1" #put the expected result 
    assert actual == expected  #it will return true or false 