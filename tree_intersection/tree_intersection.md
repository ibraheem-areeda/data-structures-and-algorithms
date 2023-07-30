# Code Challenge: tree_intersection 

Find common values in 2 binary trees,
Write a function called tree_intersection that takes two binary trees as parameters.
Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
    Time Complexity: The time complexity is dominated by the two recursive functions, save and check_saved, which traverse the nodes of tree1 and tree2 respectively. The time complexity of traversing the binary trees in DFS is O(n), where 'n' is the total number of nodes in each tree. In the worst case, each node's value will be inserted into the hash table, and each node's value from the second tree will be checked in the hash table. So, the overall time complexity is O(n + m), where 'n' is the number of nodes in the first tree, and 'm' is the number of nodes in the second tree.

    Space Complexity: The space complexity is determined by the hash table and the intersection list. In the hash table, at most 'n' unique node values from the first tree will be stored (where 'n' is the number of nodes in the first tree). The intersection list can store up to 'm' unique values (where 'm' is the number of nodes in the second tree). Therefore, the overall space complexity is O(n + m) due to the hash table and intersection list.

## Solution
```
def tree_intersection(tree1, tree2):
    """
    Find the intersection of values between two binary trees.
    
    Parameters:
        tree1 (BinaryTree): The first binary tree.
        tree2 (BinaryTree): The second binary tree.

    Returns:
        list: A list containing the values that are common to both trees
    """
    
    hasht = HashTable()

    def save (node):
        if node:
            hasht.set(str(node.value), 1)
            save (node.left)
            save (node.right)
    save (tree1.root)

    intersection = []

    def check_saved (node):
        if node:
            if hasht.has(str(node.value)) :
                if node.value not in intersection:
                    intersection.append(node.value)
            check_saved (node.left)
            check_saved (node.right)
    check_saved (tree2.root)

    return intersection
```