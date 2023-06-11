import pytest
from trees.trees.trees import (
    Node,
    Tnode,
    Queue,
    Tree,
    Binary_Search_Tree
)

def test_instantiate_an_empty_tree():
    tst_tree = Tree()
    actual = str(tst_tree) #call the function with the test value
    expected = "this Tree is empty" #put the expected result 
    assert actual == expected  #it will return true or false 

def test_instantiate_tree_single_root_node():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    tst_tree = Tree()
    tst_tree.root = tn1
    actual = str(tst_tree) 
    expected = "the Tree root = 10," 
    assert actual == expected  

def test_BST_add_left_child_and_right_child_properly():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.breadth_first()
    expected = [10, 8, 20, 7, 9, 15, 30]
    assert actual == expected  

def test_pre_order_traversal():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.pre_order()
    expected = [10, 8, 7, 9, 20, 15, 30]
    assert actual == expected  

def test_post_order_traversal():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.post_order()
    expected = [7, 9, 8, 15, 30, 20, 10]
    assert actual == expected 

def test_in_order_traversal():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.in_order()
    expected = [7, 8, 9, 10, 15, 20, 30]
    assert actual == expected 

def test_contains_true():
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)
    actual = brs_tst.contains(10)
    expected = True
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
    actual = brs_tst.contains(56)
    expected = False
    assert actual == expected 