# Code Challenge: Class 07: k-th value from the end of a linked list.
The task is to implement a method called "kth from end" for the Linked List class. This method takes a parameter 'k' and returns the value of the node that is k positions from the tail of the linked list. It uses the Node class and other methods from the Linked List class to locate and retrieve the desired node. This method adds the ability to access values in the linked list based on their positions from the end.

## Whiteboard Process
![](./assets/code%20challange%207.png)

## Approach & Efficiency
The approach in the provided code is to iterate through the linked list and count the number of elements while maintaining a reference to the tail of the list. Then, based on the value of `k`, it traverses the list again to find the kth element from the end.

The time complexity of this approach is O(n), where n is the number of elements in the linked list. This is because the code iterates through the list twice: once to count the elements and once to find the kth element from the end. The first iteration counts all the elements, which takes O(n) time, and the second iteration traverses a portion of the list, which takes O(n-k) time in the worst case.

The space complexity of the provided code is O(1), which means it uses constant space. This is because the code does not utilize any additional data structures or dynamically allocate memory based on the size of the input. It only uses a fixed number of variables to keep track of the count, current node, tail node, and the kth element from the end. Regardless of the size of the linked list, the amount of memory used remains constant.

## Solution
```
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
```

