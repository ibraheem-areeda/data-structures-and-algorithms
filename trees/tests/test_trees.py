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

class tnode:
    def __init__(self, value, right = None , left = None):
        self.value = value
        self.right = right
        self.left = left

class Tree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        if not self.root:
            return "this tree is empty"
        
        breadth = Queue()
        output = []
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            tn_front = breadth.dequeue()
            breadth.dequeue()
            output.append(tn_front.value)
            
            if tn_front.left:
                breadth.enqueue(tn_front.left)
            
            if tn_front.right:
                breadth.enqueue(tn_front.right)
        return output
    
    def pre_order (self):

        def _walk(root):
            print (root.value)
        if root.left:
            _walk(root.left)

        if root.right:
            _walk(root.right)

        _walk(self.root)


