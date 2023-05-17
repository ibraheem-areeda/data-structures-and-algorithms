class Node ():
    def __init__(self, value ,next_node = None):
        self.value = value
        self.pointer = next_node

    def __repr__ (self):
        return f"Node instance. value = {self.value} pointer = {self.pointer}"


class LinkedList ():
    def __init__(self,head=None):
        self.head = head
    
    def __repr__ (self):
        return f"LinkedList instance. head = {self.head}"

    def insert (self,value):
        new_node = Node(value)
        new_node.pointer = self.head
        self.head = new_node

    def includes(self,value) :
        current = self.head
        while current:
            if current.value == value: return True
            current = current.pointer
        return False

    def to_string (self) :
    
        def formater (lst):
            formatted_values = []
            for value in lst:
                formatted_value = '{ ' + value + ' }'
                formatted_values.append(formatted_value)
                formatted_string = ' -> '.join(formatted_values)
            return formatted_string + ' -> NULL'
        lst = []
        current = self.head
        while current:
            lst.append(str(current.value))
            current = current.pointer
        return formater(lst)
    
    def append (self,value) :

        if self.head == None :
             self.head = Node(value)
             return
        current = self.head
        while current:
            if current.pointer == None :
                current.pointer = Node(value)
                break
            current = current.pointer

    def insert_before(self,value,new_value):
        current = self.head
        previous = self.head
        count = 0
        if self.head.value == value : 
            self.head = Node(new_value,self.head.pointer)
            return
        while current:
            if current.value == Node(value).value:
                previous.pointer = Node(new_value,current)
            if count >= 1: 
                previous = previous.pointer
            current = current.pointer
            count = count + 1

    def insert_after(self,value,new_value):
        current = self.head
        while current:
            if current.value == value:
                current.pointer = Node(new_value,current.pointer)
                return
            else: current = current.pointer
        

if __name__=="__main__":

    
    node_4=Node (4)
    node_3=Node (3,node_4)
    node_2=Node (2,node_3)
    node_1=Node (1,node_2)
    
    linked_ltest = LinkedList (node_1)
    
    linked_ltest.insert_after(4,88)

    print(111111,linked_ltest)
