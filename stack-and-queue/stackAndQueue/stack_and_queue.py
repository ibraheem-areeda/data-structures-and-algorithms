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




