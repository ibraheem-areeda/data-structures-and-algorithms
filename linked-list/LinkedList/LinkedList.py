class Node ():
    def __init__(self, value ,pointer = None):
        self.value = value
        self.pointer = pointer

    def __repr__ (self):
        return f"Node instance. value = {self.value} pointer = {self.pointer}"


class LinkedList ():
    def __init__(self,head=None):
        self.head = head
    
    def __repr__ (self):
        return f"LinkedList instance. head = {self.head}"

    def insert (self , value):
        new_node = Node(value)
        new_node.pointer = self.head
        self.head = new_node

    def includes(self,value) :
        current = self.head
        while current:
            if current.value == value: return True
            current = current.pointer
        return False
       


if __name__=="__main__":

    a = Node(1,Node(2))
    b = Node(2,Node(3))
    c = Node(3,Node(4))
    d = Node(4)
    new_ntst = LinkedList(a)
    print(new_ntst)
    print(new_ntst.includes(2))