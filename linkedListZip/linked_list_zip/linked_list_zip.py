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
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.pointer
        return result

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

    def kth_from_end (self,k):
        count = 0
        current = self.head
        if current.pointer == None: return "the linked list has only one value"
        while current:
            count += 1
            tail = current
            current = current.pointer
        if k == 0 : return tail
        if k >= count : return f"the length of linked list is {count-1}, please inter equal or a lower number"
        if k < (-count):return f"the length of linked list is {count-1}, please a reasonable input number"
        current = self.head
        if k>0 :
            print ("ok")
            k_steps = count - k
            while k_steps != 0 :
                k_value = current
                current = current.pointer
                k_steps -= 1
            return k_value
        else:
            k_steps = count - (count + k)
            while k_steps != 0 :
                    k_value = current
                    current = current.pointer
                    k_steps -= 1
        return k_value
    
### out if the class ###
def linked_list_zip(list1,list2): # function out of the class
            
        if not list1.head:
            return list2
        
        if not list2.head:
            return list1

        current1 = list1.head
        current2 = list2.head

        new_head = Node(current1.value)
        current = new_head

        current1 = current1.pointer

        while current1 and current2:
            current.pointer = current2
            current2 = current2.pointer
            current = current.pointer

            current.pointer = current1
            current1 = current1.pointer
            current = current.pointer

        if current1:
            current.pointer = current1
        elif current2:
            current.pointer = current2

        return LinkedList(new_head)

        

if __name__=="__main__":
    
    node_4=Node (4)
    node_3=Node (3,node_4)
    node_2=Node (2,node_3)
    node_1=Node (1,node_2)

    node_5=Node (5)
    node_6=Node (6,node_5)
    node_7=Node (7,node_6)
    node_8=Node (8,node_7)
    
    linked_ltest = LinkedList (node_1)
    linked_ltest2 = LinkedList (node_8)

    print(111111,linked_ltest)
    print(22222,linked_ltest2)
    print(444444,linked_list_zip(linked_ltest,linked_ltest2))
