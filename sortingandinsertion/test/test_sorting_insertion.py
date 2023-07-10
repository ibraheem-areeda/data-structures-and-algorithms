import pytest
from sortingandinsertion.sortinginsertion.sorting_insertion import insert, insertion_sort

@pytest.fixture
def sorted_list():
    return [1, 3, 5, 7]

def test_insert_in_middle(sorted_list):
    value = 4
    insert(sorted_list, value)
    assert sorted_list == [1, 3, 4, 5, 7]

def test_insert_at_beginning(sorted_list):
    value = 0
    insert(sorted_list, value)
    assert sorted_list == [0, 1, 3, 5, 7]


def test_insertion_sort_empty_list():
    input_list = []
    expected_output = []
    assert insertion_sort(input_list) == expected_output

def test_insertion_sort_sorted_list():
    input_list = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == expected_output

def test_insertion_sort_unsorted_list():
    input_list = [5, 2, 7, 1, 3]
    expected_output = [1, 2, 3, 5, 7]
    assert insertion_sort(input_list) == expected_output


