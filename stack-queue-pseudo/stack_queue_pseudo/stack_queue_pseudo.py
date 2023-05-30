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

    def __str__(self):
        """
        Return a string representation of the Node.

        Returns:
            A string representation of the value stored in the Node.
        """
        return f"{self.value}"


class Stack:
    def __init__(self, top=None):
        """
        Initialize a new Stack object.

        Args:
            top: The top node of the stack. Default is None.
        """
        self.top = top

    def __str__(self):
        """
        Return a string representation of the Stack.

        Returns:
            A string representation of the value stored in the top node of the Stack.
            If the stack is empty, returns "This stack is empty".
        """
        if self.top is None:
            return "this stack is empty"
        return f"the stack top value = {self.top.value} next value = {self.top.next_}"

    def push(self, value):
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        self.top = Node(value, self.top)

    def pop(self):
        """
        Removes and returns the value from the top of the stack.

        Returns:
            The value that was removed from the top of the stack.
            If the stack is empty, returns "This stack is empty".
        """
        if self.top is None:
            raise Exception("this stack is empty")
        temp = self.top
        self.top = temp.next_
        temp.next_ = None
        return temp.value

    def peek(self):
        """
        Returns the value from the top of the stack without removing it.

        Returns:
            The value from the top of the stack.
            If the stack is empty, raise AttributeError and print "This stack is empty".
        """
        return self.top.value


class PseudoQueue():
    """
    PseudoQueue represents a queue implemented using two stacks.

    The class provides methods to enqueue and dequeue elements from the queue.

    Attributes:
    - stack_in (Stack): Stack used for enqueue operation.
    - stack_out (Stack): Stack used for dequeue operation.

    Methods:
    - enqueue(value): Inserts an element into the queue.
    - dequeue(): Removes and returns the element from the front of the queue.
    """
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, value):
        """
        Inserts an element into the queue.

        Args:
        - value: The value to be inserted.
        """
        self.stack_in.push(value)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
        - The element at the front of the queue.

        Raises:
        - Exception : If the queue is empty.
        """
        temp = self.stack_in.top
        while temp:
            self.stack_in.top = temp.next_
            self.stack_out.push(temp)
            temp = temp.next_
        self.stack_out.pop()
        temp = self.stack_out.top
        while temp:
            self.stack_out.top = temp.next_
            self.stack_in.push(temp)
            temp = temp.next_


    
if __name__=="__main__":
    v3 = 3
    v2 = Node(2,Node(v3))
    v1 = Node(1,Node(v2))
    tset = PseudoQueue()
    tset.enqueue(v1)
    tset.enqueue(v2)


    print (tset.stack_in)
    print (tset.stack_out)

