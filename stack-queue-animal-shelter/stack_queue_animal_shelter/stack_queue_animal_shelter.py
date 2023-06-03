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
    def __init__(self, front=None):
        """
        Initialize a new Queue object.

        Args:
            front: The front node of the queue. Default is None.
        """
        self.front = front

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
            current = self.front
            while current.next_:
                current = current.next_
            current.next_ = node

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

class Animal():
    def __init__ (self,name,species,next_=None):
        self.name = name
        self.species = species
        self.next_ = next_
        self.node = Node(Animal,self.next_)


class AnimalShelter ():
    def __init__(self):
        cat_queue = Queue()
        dog_queue = Queue()
    def enqueue (animal):
        if not isinstance(animal, Animal) : return "please enter dog or cat"



    
if __name__ == "__main__":
    meme = Animal("meme" , "cat")
    print(meme.node.value.name)
    print(AnimalShelter.enqueue(meme))
