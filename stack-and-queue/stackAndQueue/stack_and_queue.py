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
    def __init__(self , front = None , back = None):
       pass 

