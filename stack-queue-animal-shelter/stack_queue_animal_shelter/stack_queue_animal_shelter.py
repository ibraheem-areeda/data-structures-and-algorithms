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
    def __init__ (self, name, species):
        """
        Initialize an Animal instance with a name and species.

        Args:
            name (str): The name of the animal.
            species (str): The species of the animal.
        """
        self.name = name
        self.species = species

    def __str__(self):
        """
        Returns a string representation of the Animal object.

        Returns:
            str: The string representation of the Animal object, including its name and species.
        """
        return f"Animal name is {self.name}, Animal species is {self.species}"


class AnimalShelter():
    def __init__(self):
        """
        Initialize an AnimalShelter object.

        This object keeps track of cat and dog queues.
        """
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        """
        Enqueue an animal into the appropriate queue.

        Args:
            animal (Animal): The Animal instance to be enqueued.

        Returns:
            str or None: If the animal is not an instance of Animal, or if the species or name is invalid, returns an error message. Otherwise, returns None.
        """
        if not isinstance(animal, Animal):
            return "Please enter an animal instance."
        if animal.species != "cat" and animal.species != "dog":
            return "Please enter 'cat' or 'dog' for the animal species."
        if type(animal.name) is not str:
            return "Please enter the animal name correctly."
        if animal.species == "cat":
            self.cat_queue.enqueue(Node(animal))
        else:
            self.dog_queue.enqueue(Node(animal))

    def dequeue(self, pref):
        """
        Dequeue an animal from the appropriate queue based on preference.

        Args:
            pref (str): The preferred species ('cat' or 'dog') for dequeuing.

        Returns:
            str or None: If the preference is not valid, returns an error message. Otherwise, returns None.
        """
        if pref != "cat" and pref != "dog":
            return "Please enter 'cat' or 'dog' as the preference."
        if pref == "cat":
            self.cat_queue.dequeue()
        else:
            self.dog_queue.dequeue()

            














    
if __name__ == "__main__":
    meme = Animal("meme" , "cat")
    rex = Animal("rex","dog")
    leya = Animal("leya","cat")
    leo_shelter = AnimalShelter()
    print(meme.species)
    leo_shelter.enqueue(meme)
    leo_shelter.enqueue(rex)
    leo_shelter.enqueue(leya)
    print(leo_shelter.cat_queue)
    print(leo_shelter.dog_queue)
    print(meme.name)
    print(leo_shelter.dequeue("cat"))
    print(leo_shelter.cat_queue)