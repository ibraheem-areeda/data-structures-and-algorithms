import pytest
from sorting_Merge.sorting_merge import merge_sort,merge

import pytest

# Unit tests for merge_sort()
def test_merge_sort_case1():
    arr = [5, 2, 9, 1, 7]
    merge_sort(arr)
    assert arr == [1, 2, 5, 7, 9]

def test_merge_sort_case2():
    arr = [3, 8, 1, 6, 4, 2]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 6, 8]

def test_merge_sort_case3():
    arr = [9, 5, 2, 7, 1]
    merge_sort(arr)
    assert arr == [1, 2, 5, 7, 9]


# Unit tests for merge()
def test_merge_case1():
    left = [2, 4, 6]
    right = [1, 3, 5]
    arr = [0] * (len(left) + len(right))
    merge(left, right, arr)
    assert arr == [1, 2, 3, 4, 5, 6]

def test_merge_case2():
    left = [7, 9]
    right = [1, 3, 5, 8]
    arr = [0] * (len(left) + len(right))
    merge(left, right, arr)
    assert arr == [1, 3, 5, 7, 8, 9]

def test_merge_case3():
    left = [4, 6, 8, 10]
    right = [1, 3, 5, 7, 9]
    arr = [0] * (len(left) + len(right))
    merge(left, right, arr)
    assert arr == [1, 3, 4, 5, 6, 7, 8, 9, 10]
