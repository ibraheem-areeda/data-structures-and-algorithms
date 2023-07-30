import pytest
from tree_intersection.tree_intersection import tree_intersection , Binary_Search_Tree , Tnode , Tree

def test_tree_intersection_with_empty_trees():
    tree1 = Binary_Search_Tree()
    tree2 = Binary_Search_Tree()
    assert tree_intersection(tree1, tree2) == []

def test_tree_intersection_with_no_common_elements():
    tree1 = Binary_Search_Tree()
    l = Tnode(3)
    r = Tnode(2)
    tn1 = Tnode(1,r,l)

    tree2 = Binary_Search_Tree()
    l = Tnode(4)
    r = Tnode(5)
    tn2 = Tnode(6,r,l)

    assert tree_intersection(tree1, tree2) == []

def test_tree_intersection_with_common_elements():

    l = Tnode(3)
    r = Tnode(2)
    tn1 = Tnode(1,r,l)
    tree1 = Binary_Search_Tree(tn1)
    tree1.add(4)

    l = Tnode(4)
    r = Tnode(5)
    tn2 = Tnode(6,r,l)
    tree2 = Binary_Search_Tree(tn2)
    tree2.add(3)

    assert tree_intersection(tree1, tree2) == [4, 3]

def test_tree_intersection_with_single_common_element():

    l = Tnode(3)
    r = Tnode(2)
    tn1 = Tnode(1,r,l)
    tree1 = Binary_Search_Tree(tn1)

    l = Tnode(4)
    r = Tnode(5)
    tn2 = Tnode(6,r,l)
    tree2 = Binary_Search_Tree(tn2)
    tree2.add(3)

    assert tree_intersection(tree1, tree2) == [3]



