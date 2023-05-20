class Node:
    def __init__ (self , value , next_ = None):
        self.value = value
        self.next_ = next_

class stack:
    def __init__ (self, top = None):
        self.top = top

    def push (self , value):
        self.top = Node(value,self.top.next_)

    def pop (self):
        if self.top == None: return "this stack is empty"
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
        if self.front == None: return "this queue is empty"
        temp = self.front
        self.front = temp.next_
        temp.next_ = None

    def peek (self):
        if self.front == None: return "this queue is empty"
        else : return self.front.value

    def is_empty(self):
        if self.front == None: return True
        else: return False



