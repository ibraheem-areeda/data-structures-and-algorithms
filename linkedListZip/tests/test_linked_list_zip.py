import pytest
from linked_list_zip.linked_list_zip import (
  LinkedList,
)
##############################################################
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    return linked_list
###############################################################
# Test cases
def test_linked_list_zip_same_length():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [1, 2, 3, 4, 5, 6]

def test_linked_list_zip_first_list_longer():
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4, 6])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [1, 2, 3, 4, 5, 6, 7, 9]

def test_linked_list_zip_second_list_longer():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6, 8, 10])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [1, 2, 3, 4, 5, 6, 8, 10]

def test_linked_list_zip_first_list_empty():
    list1 = create_linked_list([])
    list2 = create_linked_list([2, 4, 6])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [2, 4, 6]

def test_linked_list_zip_second_list_empty():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [1, 3, 5]

def test_linked_list_zip_empty_lists():
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == []

def test_linked_list_zip_single_node_lists():
    list1 = create_linked_list([1])
    list2 = create_linked_list([2])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [1, 2]

def test_linked_list_zip_large_lists():
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4, 6, 8, 10])
    result = LinkedList.linked_list_zip(list1, list2)
    assert result.to_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
