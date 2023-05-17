# Code Challenge 6 : linked-list-insertions

The challenge want us to implement the following methods for the Linked List class we did at the last challenge:

1. `append(new_value)`: Adds a new node with the given value to the end of the list.

2. `insert_before(value, new_value)`: Adds a new node with the given new value immediately before the first node that has the specified value.

3. `insert_after(value, new_value)`: Adds a new node with the given new value immediately after the first node that has the specified value.


## Whiteboard Process
Here I will attach the pictures of the 3 whiteboards I did for the 3 methods in the past description
- Append 
![append](./assets/new%20append.png)

- Insert Befor 
![insert_befor](./assets/new%20insert%20befor.png)

- Insert After
![insert_after](./assets/new%20insert%20after.png)

## Approach & Efficiency
The approach taken is to implement a Linked List using a Node class and a LinkedList class.

The Node class represents individual nodes in the Linked List. Each node has a value property to store the value it holds and a pointer property that points to the next node in the list. The __repr__ method is overridden to provide a string representation of the Node instance.

The LinkedList class represents the overall Linked List structure. It has a head property that points to the first node in the list. The class provides the following new methods:

- append: Adds a new node with the given value at the end of the list. It iterates through the list until it finds the last node and then appends the new node. The time complexity for this approach is O(n) since it may need to traverse the entire list in the worst case, but the space complexity = O(1) : because it requires a constant amount of additional space

 - insert_before: Inserts a new node with a new value before the first occurrence of a specified value in the list. It iterates through the list, finds the target value, and inserts the new node before it. The time complexity for this approach is O(n) since it may need to traverse the entire list to find the target value, but the space complexity = O(1) : because it requires a constant amount of additional space

 - insert_after: Inserts a new node with a new value after the first occurrence of a specified value in the list. It iterates through the list, finds the target value, and inserts the new node after it. The time complexity for this approach is O(n) since it may need to traverse the entire list to find the target value, but the space complexity = O(1) : because it requires a constant amount of additional space

The space complexity of the code over all is O(n) since it stores n nodes in the Linked List.

## Solution
```
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
```

