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

def test_head_point_to_the_first_node(linked_ltest):
    actual =  linked_ltest
    expected ="LinkedList instance. head = Node instance. value = 1"
    act = str(actual)
    assert act[0:52] == expected  

def test_insert_multiple_nodes(linked_ltest):
    actual =  linked_ltest
    expected ="LinkedList instance. head = Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = None"
    act = str(actual)
    assert act == expected  

def test_insert_multiple_nodes_by_method (linked_ltest_insert):
    actual =  linked_ltest_insert
    expected ="LinkedList instance. head = Node instance. value = 4 pointer = Node instance. value = 3 pointer = Node instance. value = 2 pointer = 1"
    act = str(actual)
    assert act == expected  

def test_true_when_finding_value(linked_ltest):
    actual =  linked_ltest.includes(2)
    expected = True
    assert actual == expected  

def test_false_when_not_finding_value(linked_ltest):
    actual =  linked_ltest.includes(8)
    expected = False
    assert actual == expected  

def test_collection_of_all_values(linked_ltest):
    actual =  linked_ltest.to_string()
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"
    assert actual == expected    

    
#######################
# Fixtures
#######################


@pytest.fixture
def linked_ltest():
    node_4=Node (4)
    node_3=Node (3,node_4)
    node_2=Node (2,node_3)
    node_1=Node (1,node_2)
    linked_ltest = LinkedList (node_1)
    return linked_ltest

@pytest.fixture
def linked_ltest_insert():
    linked_ltest = LinkedList (1)
    linked_ltest.insert(2)
    linked_ltest.insert(3)    
    linked_ltest.insert(4)    
    return linked_ltest
