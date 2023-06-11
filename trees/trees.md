# Binary Tree and BST
The given code summary describes the implementation of classes for Node, Binary Tree, and Binary Search Tree. The Node class represents a node in a binary tree. The Binary Tree class defines methods for three depth-first traversals: pre-order, in-order, and post-order. The Binary Search Tree class is a subclass of the Binary Tree class and includes additional methods for adding nodes in the correct location and checking if a value exists in the tree.

## Whiteboard Process
not requierd for this code challange 

## Approach & Efficiency
### Efficiency
The provided code implements a binary search tree (BST) data structure. The `add` method adds a new node with the given value to the tree by recursively traversing and comparing values. It starts at the root and moves to the left or right child nodes based on the comparison. If a child node is empty, the new node is inserted at that position. The `contains` method checks if the tree contains a node with a given value. It also uses recursive traversal to compare values and navigate through the tree. If the value is found, it returns `True`; otherwise, it returns `False`. The efficiency of the code depends on the balance of the tree. In the worst case, when the tree is heavily unbalanced, the time complexity for both methods can be O(n) where n is the number of nodes. However, in balanced trees, the average and best-case time complexity is O(log n) as the tree's structure allows for efficient search and insertion operations.
### Approach
The approach used in the code follows a recursive strategy for traversal and comparison. This approach simplifies the implementation by utilizing the BST property where values less than the current node are found in the left subtree and values greater than the current node are found in the right subtree. However, the code does not account for potential errors or edge cases, such as handling duplicate values or validating inputs. It also uses a global variable `result` in the `contains` method, which can be improved by using a different approach for returning the result or by modifying the method to pass the result as a parameter. Overall, the code provides a basic implementation of a binary search tree but may require further enhancements to handle additional scenarios and improve efficiency.
## Solution
```
class Tnode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, value, right=None, left=None):
        """
        Initializes a tree node with the given value and optional left and right child nodes.

        Args:
            value: The value of the node.
            right: The right child node (default: None).
            left: The left child node (default: None).
        """
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            A string representation of the node.
        """
        if self.value is None:
            return "This tree node is empty"

        if self.right.value is None:
            return "This node's right child is empty"

        if self.left.value is None:
            return "This node's left child is empty"

        return f"The tree node value = {self.value}, its left node value = {self.left.value}, its right node value = {self.right.value}"


class Tree:
    """
    Represents a binary tree.
    """

    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def __str__(self):
        """
        Returns a string representation of the tree.

        Returns:
            A string representation of the tree.
        """
        if self.root is None:
            return "this Tree is empty"
        return f"the Tree root = {self.root.value},"

    def breadth_first(self):
        """
        Performs a breadth-first traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the breadth-first traversal order.
        """
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        """
        Performs a pre-order traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the pre-order traversal order.
        """
        output = []

        def _walk(root):
            output.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        """
        Performs an in-order traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the in-order traversal order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            output.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self):
        """
        Performs a post-order traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the post-order traversal order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            output.append(root.value)

        _walk(self.root)
        return output


class Binary_Search_Tree(Tree):
    """
    Represents a binary search tree, which is a specialized version of a binary tree.
    """

    def __init__(self, root=None):
        """
        Initializes a binary search tree with the given root.

        Args:
            root: The root node of the binary search tree (default: None).
        """
        self.root = root

    def __str__(self):
        """
        Returns a string representation of the binary search tree.

        Returns:
            A string representation of the binary search tree.
        """
        if self.root is None:
            return "This binary tree is empty"

        return f"The tree root = {self.root.value}"

    def add(self, value):
        """
        Adds a node with the given value to the binary search tree.

        Args:
            value: The value of the node to be added.
        """
        tn_value = Tnode(value)

        def _walk(root):
            if root:
                if root.value < tn_value.value:
                    if root.right is not None:
                        _walk(root.right)
                    else:
                        root.right = Tnode(value)

                if root.value > tn_value.value:
                    if root.left is not None:
                        _walk(root.left)
                    else:
                        root.left = Tnode(value)

        _walk(self.root)

    def contains(self, value):
        """
        Checks if the binary search tree contains a node with the given value.

        Args:
            value: The value to search for in the binary search tree.

        Returns:
            True if the binary search tree contains a node with the given value, False otherwise.
        """
        if self.root.value == value:
            return True

        def _walk(root):
            global result
            if root:
                if root.value < value:
                    if not root.right:
                        result = False
                        return result
                    if root.right.value == value:
                        result = True
                        return result
                    else:
                        _walk(root.right)

                if root.value > value:
                    if not root.left:
                        result = False
                        return result
                    if root.left.value == value:
                        result = True
                        return result
                    else:
                        _walk(root.left)

        _walk(self.root)
        return result
```
