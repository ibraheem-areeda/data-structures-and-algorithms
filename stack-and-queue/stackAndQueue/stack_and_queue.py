class Node:
    def __init__ (self , value , next_ = None):
        self.value = value
        self.next_ = next_

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

    def enqueue (self , value):
        self.back = Node(value)

    def dequeue(self):
        if self.front.value == None: return "this queue is empty"
        temp = self.front
        self.front = temp.next_
        temp.next_ = None

    def peek (self):
        if self.front == None: return "this queue is empty"
        else : return self.front.value

    def is_empty(self):
        if self.front == None: return True
        else: return False


if __name__=="__main__":
    node1 = Node(1)
    test_stack = stack(node1)
    test_stack.push(2)
    test_stack.push(3)
    print(test_stack.top.value)
    test_stack.pop()
    print(test_stack.top.value)
