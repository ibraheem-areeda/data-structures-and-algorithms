class Node:
    def __init__(self, value, next_=None):
        """
        Initialize a new Node object.

        Args:
            value: The value to be stored in the node.
            next_: Reference to the next node in the linked list. Default is None.
        """
        self.value = value
        self.next_ = next_
class Queue:
    def __init__(self, front=None, back = None):
        """
        Initialize a new Queue object.

        Args:
            front: The front node of the queue. Default is None.
        """
        self.front = front
        self.back = back

    def __str__(self):
        """
        Return a string representation of the Queue.

        Returns:
            A string representation of the value stored in the front node of the Queue.
            If the queue is empty, returns "This queue is empty".
        """
        if self.front is None:
            return "this queue is empty"
        return f"the queue front = {self.front.value},"

    def enqueue(self, value):
        """
        Adds a value to the end of the queue.

        Args:
            value: The value to be added to the queue.
        """
        node = Node(value)
        if self.front is None:
            self.front = node
        else:
            self.back = self.front
            while self.back.next_:
                self.back = self.back.next_
            self.back.next_ = node

    def dequeue(self):
        """
        Removes and returns the value from the front of the queue.

        Returns:
            The value that was removed from the front of the queue.
            If the queue is empty, returns "This queue is empty".
        """
        if self.front is None:
            raise Exception("this queue is empty")
        temp = self.front.value
        self.front = self.front.next_
        return temp

    def peek(self):
        """
        Returns the value from the front of the queue without removing it.

        Returns:
            The value from the front of the queue.
            If the queue is empty, returns "This queue is empty".
        """
        if self.front is None:
            raise Exception("this queue is empty")
        return f"the queue front = {self.front.value},"

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None
    
    def to_string (self):
        temp = self.front
        string = ""
        while temp:
            string += str(temp.value)
            temp = temp.next_
        return string

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


if __name__=="__main__":
    l = Tnode(8)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    brs_tst = Binary_Search_Tree(tn1)
    print(brs_tst.root)
    brs_tst.add(7)
    brs_tst.add(9)
    brs_tst.add(15)
    brs_tst.add(30)

    print(brs_tst.post_order())
    print(brs_tst.contains(10))
    print(brs_tst.contains(8))
    print(brs_tst.contains(20))
    print(brs_tst.contains(8))
    print(brs_tst.contains(10))
    print(brs_tst.contains(20))
    print(brs_tst.contains(7))
    print(brs_tst.contains(9))
    print(brs_tst.contains(2))
    print(brs_tst.contains(606))
    print(brs_tst.contains(63333333333))