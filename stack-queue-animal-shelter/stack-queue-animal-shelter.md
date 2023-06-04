# Code Challenge 12 : First-in, First out Animal Shelter.
The tasl is to write `AnimalShelter` class represents a shelter that holds dogs and cats using a first-in, first-out approach. It has an `enqueue` method to add animals to the shelter, which must have species (cat or dog) and name properties. The `dequeue` method removes and returns an animal based on a specified preference (dog or cat). If the preference is not valid, null or an appropriate null-like value is returned.
## Whiteboard Process
![](./asstets/enqueue%20animal.png)
![](./asstets/dequeue%20animal.png)
## Approach & Efficiency
 - Enqueue Operation: The enqueue method has a time complexity of O(1) as it performs a constant number of operations regardless of the size of the queues. The checks before enqueueing an animal have constant time complexity as well.
 - Dequeue Operation: The dequeue method has a time complexity of O(1) as it performs a constant number of operations regardless of the size of the queues.    

The code is maintaing a separate queues for cats and dogs, allowing enqueue and dequeue operations to be performed in constant time. The code also includes input validation to ensure that only valid animals are enqueued, enhancing the robustness of the implementation, the space complexity is O(1) because for each time we call it it will do 1 insertion to the memoey.
## Solution
```
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
```