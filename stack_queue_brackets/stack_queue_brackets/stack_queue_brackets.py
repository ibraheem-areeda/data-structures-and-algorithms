import re
class Node:
    def __init__(self, value, next_=None):
        """
        Initialize a new Node object.

        Args:
            value: The value to be stored in the node.
            next_: Reference to the next node in the linked list. Default is None.
        """
        self.value = value
        self.next_ = next_

    def __str__(self):
        """
        Return a string representation of the Node.

        Returns:
            A string representation of the value stored in the Node.
        """
        return f"{self.value}"
    
class Queue:
    def __init__(self, front=None, back = None):
        """
        Initialize a new Queue object.

        Args:
            front: The front node of the queue. Default is None.
        """
        self.front = front
        self.back = back

    def __str__(self):
        """
        Return a string representation of the Queue.

        Returns:
            A string representation of the value stored in the front node of the Queue.
            If the queue is empty, returns "This queue is empty".
        """
        if self.front is None:
            return "this queue is empty"
        return f"the queue front = {self.front.value},"

    def enqueue(self, value):
        """
        Adds a value to the end of the queue.

        Args:
            value: The value to be added to the queue.
        """
        node = Node(value)
        if self.front is None:
            self.front = node
        else:
            self.back = self.front
            while self.back.next_:
                self.back = self.back.next_
            self.back.next_ = node

    def dequeue(self):
        """
        Removes and returns the value from the front of the queue.

        Returns:
            The value that was removed from the front of the queue.
            If the queue is empty, returns "This queue is empty".
        """
        if self.front is None:
            raise Exception("this queue is empty")
        temp = self.front.value
        self.front = self.front.next_
        return temp

    def peek(self):
        """
        Returns the value from the front of the queue without removing it.

        Returns:
            The value from the front of the queue.
            If the queue is empty, returns "This queue is empty".
        """
        if self.front is None:
            raise Exception("this queue is empty")
        return f"the queue front = {self.front.value},"

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None
    
    def to_string (self):
        temp = self.front
        string = ""
        while temp:
            string += str(temp.value)
            temp = temp.next_
        return string

class Stack:
    def __init__(self, top=None):
        """
        Initialize a new Stack object.

        Args:
            top: The top node of the stack. Default is None.
        """
        self.top = top

    def __str__(self):
        """
        Return a string representation of the Stack.

        Returns:
            A string representation of the value stored in the top node of the Stack.
            If the stack is empty, returns "This stack is empty".
        """
        if self.top is None:
            return "this stack is empty"
        return f"the stack top value = {self.top.value}"

    def push(self, value):
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        self.top = Node(value, self.top)

    def pop(self):
        """
        Removes and returns the value from the top of the stack.

        Returns:
            The value that was removed from the top of the stack.
            If the stack is empty, returns "This stack is empty".
        """
        if self.top is None:
            raise Exception("this stack is empty")
        temp = self.top
        self.top = temp.next_
        temp.next_ = None
        return temp.value

    def peek(self):
        """
        Returns the value from the top of the stack without removing it.

        Returns:
            The value from the top of the stack.
            If the stack is empty, raise AttributeError and print "This stack is empty".
        """
        if self.top is None:
            raise Exception("this stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None

def validate_brackets (string):
    queue1 = Queue()
    queue2 = Queue()
    validation_arr = ["{}","()","[]"]
    empty_brackets = re.sub(r"[^\]\[\(\)\{\}]+", "" , string )

    print("all",empty_brackets)
    if len(empty_brackets) % 2 != 0 :return False
    for bracket in range(len(empty_brackets)):
        queue1.enqueue(empty_brackets[bracket])

    queue1.dequeue()
    i=0


    while queue1.front :
        print("theloop is", queue1.front is not None)
        print("iiiiiiiiiii",i)
        print("befor if statment empty_brackets[i]",empty_brackets[0], "q1=", queue1.to_string(),"q1.front",queue1.front.value, "q2=",queue2.to_string())
        if empty_brackets[0]+ queue1.front.value in  validation_arr :
            i += 1
            print("ttttttttttt",empty_brackets[0]+ queue1.front.value)
            queue1.dequeue()
            print("afer deqe for match",queue1.to_string())
            if queue1.front :
                empty_brackets = queue1.front.value
                queue1.dequeue()
                print("afer deqe for compare",queue1.to_string())
            else:
                return True


            print("ok")
            print("after True ","q2=",queue2.to_string(),"q1=",queue1.to_string(),"empty_brackets[i]",empty_brackets[0])
        else:
            print("q1",queue1.to_string())

            test = queue1.to_string()
            # print(test[0],test[1],test[2] )
            if test[0] + test[2] in validation_arr and test[0] != test[1] and test[2] != test[1]:
                return False

            print("after else comp[0]",empty_brackets[0])
            temp = queue1.front
            queue1.dequeue()
            queue2.enqueue(temp)
            print("after False -> deque[this is queue1]",queue1.to_string())
            print("Q2",queue2.to_string())

    while queue2.front:
        temp = queue2.front
        queue2.dequeue()
        queue1.enqueue(temp)
        print("nnnnnnnnnode",queue1.front.value)

    while queue1.front :
        if str(queue1.front.value) + empty_brackets[0] in validation_arr :
            queue1.dequeue()
            if queue1.front :
                empty_brackets = queue1.front.value
                queue1.dequeue()
                print("afer deqe for compare",queue1.to_string())
            else:
                    return True



if __name__ == "__main__":
    print(validate_brackets("{}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("()[[Extra Characters]]"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("{}{Code}[Fellows](())"))
    print(validate_brackets("[({}]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))


