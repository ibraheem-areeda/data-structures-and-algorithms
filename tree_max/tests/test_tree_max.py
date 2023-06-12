import pytest
from tree_max.tree_max.tree_max import(
    Node,
    Tnode,
    Queue,
    Tree,
    Binary_Search_Tree
)

def test_BST_add_left_child_and_right_child_properly():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.tree_max()
    expected = 30
    assert actual == expected  

def test_pre_order_traversal():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(55)
    actual = brs_tst.tree_max()
    expected = 55
    assert actual == expected  

def test_post_order_traversal():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(7)

    actual = brs_tst.tree_max()
    expected = 20
    assert actual == expected 

def test_in_order_traversal():
    l = Tnode(8)
    r = Tnode(-1)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(1)
    brs_tst.add(0)
    brs_tst.add(-5)
    actual = brs_tst.tree_max()
    expected = 10
    assert actual == expected 

def test_contains_true():
    l = Tnode(1)
    r = Tnode(2)
    tn1 = Tnode(3,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(4)
    brs_tst.add(5)
    brs_tst.add(6)
    brs_tst.add(2)
    actual = brs_tst.tree_max()
    expected = 6
    assert actual == expected 

def test_contains_False():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.tree_max()
    expected = 30
    assert actual == expected 
