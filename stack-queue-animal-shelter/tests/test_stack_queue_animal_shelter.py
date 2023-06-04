import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import (Node,Queue,Animal,AnimalShelter)

def test_animal_is_instance_from_the_class():
    meme = {
        "name" : "meme",
        "species" : "cat"
            }
    test_shelter = AnimalShelter()
    actual = test_shelter.enqueue(meme) #call the function with the test value
    expected = "Please enter an animal instance." #put the expected result 
    assert actual == expected  #it will return true or false 

def test_animal_species_cat_or_dog():
    masha = Animal("masha","cow")
    test_shelter = AnimalShelter()
    actual = test_shelter.enqueue(masha)
    expected = "Please enter 'cat' or 'dog' for the animal species."   
    assert actual == expected

def test_if_animal_name_is_string():
    leya = Animal(123,"cat")
    test_shelter = AnimalShelter()
    actual = test_shelter.enqueue(leya)
    expected = "Please enter the animal name correctly."   
    assert actual == expected

def test_enqueue_cat():
    meme = Animal("meme" , "cat")
    test_shelter = AnimalShelter()
    test_shelter.enqueue(meme)
    actual = str(test_shelter.cat_queue)
    expected = "the queue front = Animal name is meme, Animal species is cat,"   
    assert actual == expected

def test_enqueue_dog():
    rex = Animal("rex" , "dog")
    test_shelter = AnimalShelter()
    test_shelter.enqueue(rex)
    actual = str(test_shelter.dog_queue)
    expected = "the queue front = Animal name is rex, Animal species is dog,"   
    assert actual == expected

def test_dequeue_dog():
    meme = Animal("meme" , "cat")
    rex = Animal("rex","dog")
    leya = Animal("leya","cat")
    pablo = Animal("pablo","dog")
    test_shelter = AnimalShelter()
    test_shelter.enqueue(meme)
    test_shelter.enqueue(rex)
    test_shelter.enqueue(leya)
    test_shelter.enqueue(pablo)
    test_shelter.dequeue("dog")
    actual = str(test_shelter.dog_queue)
    expected = "the queue front = Animal name is pablo, Animal species is dog,"   
    assert actual == expected

def test_dequeue_cat():
    meme = Animal("meme" , "cat")
    rex = Animal("rex","dog")
    leya = Animal("leya","cat")
    pablo = Animal("pablo","dog")
    test_shelter = AnimalShelter()
    test_shelter.enqueue(meme)
    test_shelter.enqueue(rex)
    test_shelter.enqueue(leya)
    test_shelter.enqueue(pablo)
    test_shelter.dequeue("cat")
    actual = str(test_shelter.cat_queue)
    expected = "the queue front = Animal name is leya, Animal species is cat,"   
    assert actual == expected

def test_dequeue_not_cat_or_dog():
    meme = Animal("meme" , "cat")
    rex = Animal("rex","dog")
    leya = Animal("leya","cat")
    pablo = Animal("pablo","dog")
    test_shelter = AnimalShelter()
    test_shelter.enqueue(meme)
    test_shelter.enqueue(rex)
    test_shelter.enqueue(leya)
    test_shelter.enqueue(pablo)
    test_shelter.dequeue("cat")
    actual = test_shelter.dequeue("cow")
    expected = "Please enter 'cat' or 'dog' as the preference."   
    assert actual == expected
