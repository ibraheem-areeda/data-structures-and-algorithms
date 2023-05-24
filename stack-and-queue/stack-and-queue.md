# stack-and-queue
The task is to implement a Stack and a Queue using a Linked List. 
The Stack class has a "top" property and supports push, pop, peek, and is_empty operations. 
The Queue class has a "front" property and supports enqueue, dequeue, peek, and is_empty operations. 
Both classes use the Node class to represent the nodes in the Linked List .

## Whiteboard Process
not required for this challenge

## Approach & Efficiency
Here's a table summarizing the methods in the Queue class, along with their time and space complexity:

| Method   | Description                                                  | Time Complexity | Space Complexity |
|----------|--------------------------------------------------------------|-----------------|------------------|
| enqueue  | Adds a new node to the back of the queue                     | O(n)            | O(1)             |
| dequeue  | Removes and returns the value from the front of the queue    | O(1)            | O(1)             |
| peek     | Returns the value of the node at the front of the queue      | O(1)            | O(1)             |
| is_empty | Checks if the queue is empty                                 | O(1)            | O(1)             |

Here's a table summarizing the methods in the Stack class you provided, along with their time and space complexity:

| Method   | Description                                                  | Time Complexity | Space Complexity |
|----------|--------------------------------------------------------------|-----------------|------------------|
| push     | Adds a new node with the specified value to the top of the stack | O(1)            | O(1)             |
| pop      | Removes and returns the value from the top of the stack       | O(1)            | O(1)             |
| peek     | Returns the value of the node at the top of the stack         | O(1)            | O(1)             |
| is_empty | Checks if the stack is empty                                  | O(1)            | O(1)             |

In this implementation, the time complexity for all methods is O(1) because each operation involves constant-time operations, such as updating references or accessing the value of the top node.
The space complexity is also O(1) because the amount of memory used does not depend on the size of the stack but rather on the fixed number of variables and references used to represent the stack.

## Solution
```
class Node:
    def __init__ (self , value , next_ = None):
        self.value = value
        self.next_ = next_

    def __str__ (self):
        return f"{self.value}"

class stack:
    def __init__ (self, top = None):
        self.top = top

    def __str__ (self):
        if self.top == None: return "this stack is empty"
        return f"the stack top value = {self.top.value}"

    def push (self , value):
        self.top = Node(value,self.top)

    def pop (self):
        if self.top.value == None: return "this stack is empty"
        temp = self.top
        self.top = temp.next_
        temp.next_ = None
        return temp.value
    
    def peek(self):
        if self.top == None: return "this stack is empty"
        return self.top.value
    
    def is_empty(self):
        if self.top == None: return True
        else: return False

class Queue :
    def __init__(self , front = None):
       self.front = front


    def __str__(self):
        if self.front == None: return "this queue is empty"
        else : return f"the queue front = {self.front.value},"
            
    def enqueue (self , value):
        node = Node(value)
        if self == None: self.front = node
        else:
            current = self.front
            while current.next_:
                current = current.next_
            current.next_ = node


    def dequeue(self):
        if self.front == None: return "this queue is empty"
        temp = self.front.value
        self.front = self.front.next_
        # temp.next_ = None
        return temp

    def peek (self):
        if self.front == None: return "this queue is empty"
        else : return f"the queue front = {self.front.value},"

    def is_empty(self):
        if self.front == None: return True
        else: return False

if __name__=="__main__":

    test_queue = Queue()
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.enqueue(3)
    test_queue.dequeue()
    test_queue.dequeue()

    print(test_queue)
```



