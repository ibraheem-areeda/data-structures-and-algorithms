import pytest
from linkedListKth.linkedListKth import (
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
# Linked List Insertions tests
#######################

def test_add_node_to_end (linked_ltest):
    linked_ltest.append(6)
    expected ="LinkedList instance. head = Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = Node instance. value = 6 pointer = None"
    act = str(linked_ltest)
    assert act == expected  

def test_add_node_to_end_Multi (linked_ltest):
    linked_ltest.append(6)
    linked_ltest.append(7)
    linked_ltest.append(8)
    expected ="LinkedList instance. head = Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = Node instance. value = 6 pointer = Node instance. value = 7 pointer = Node instance. value = 8 pointer = None"
    act = str(linked_ltest)
    assert act == expected  

def test_insert_before_mid_linked_list (linked_ltest):
    linked_ltest.insert_before(3,8)
    expected = "LinkedList instance. head = Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 8 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = None"
    act = str(linked_ltest)
    assert act == expected

def test_insert_before_first_node (linked_ltest):
    linked_ltest.insert_before(1,33)
    excepted = "LinkedList instance. head = Node instance. value = 33 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = None"
    act = str(linked_ltest)
    assert act == excepted

def test_insert_after_mid_linked_list (linked_ltest):
    linked_ltest.insert_after(3,55)
    excepted = "LinkedList instance. head = Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 55 pointer = Node instance. value = 4 pointer = None"
    act = str(linked_ltest)
    assert act == excepted

def test_insert_after_last_node(linked_ltest):
    linked_ltest.insert_after(4,88)
    excepted = "LinkedList instance. head = Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = Node instance. value = 88 pointer = None"
    act = str(linked_ltest)
    assert act == excepted

#######################
# Linked List kth value tests
#######################

def test_greater_than_the_length(linked_ltest):
    result = linked_ltest.kth_from_end(9)
    excepted = "the length of linked list is 3, please inter equal or a lower number"
    act = str(result)
    assert act == excepted

def  test_k_equal_length_linkedlist (linked_ltest):
    result = linked_ltest.kth_from_end(3)
    excepted = "Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = None"
    act = str(result)
    assert act == excepted

def test_Happy_Path (linked_ltest):
    result = linked_ltest.kth_from_end(2)
    excepted = "Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = None"
    act = str(result)
    assert act == excepted


def test_k_not_positive_integer(linked_ltest):
    result = linked_ltest.kth_from_end(-1)
    excepted = "Node instance. value = 1 pointer = Node instance. value = 2 pointer = Node instance. value = 3 pointer = Node instance. value = 4 pointer = None"
    act = str(result)
    assert act == excepted

def test_linked_list_size_1():
    test = LinkedList(Node(1))
    result= test.kth_from_end(0)
    excepted = "the linked list has only one value"
    act = result
    assert act == excepted

















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
