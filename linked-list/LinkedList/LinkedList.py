class Node ():
    def __init__(self, value ,pointer):
        self.value = value
        self.pointer = pointer

class LinkedList ():
    def __init__(self,head=None):
        self.head = head
    
    def insert (self , value):
        new_node = Node(value)
        new_node.pointer = self.head

