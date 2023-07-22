
import pytest
from hashtable.hashtable import HashTable

'''
'd' -> 100 * 283 = 28300 % 1024 = 652
'''



def test_hash_method():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual


def test_set_and_get():
    hashtable = HashTable()
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    assert hashtable.get("key1") == "value1"
    assert hashtable.get("key2") == "value2"

def test_retrieve():
    ht = HashTable()
    ht.set('name', 'John')
    assert ht.get('name') == 'John'

def test_null_for_nonexistent_key():
    ht = HashTable()
    assert ht.get('nonexistent_key') is None


def test_collision_handling():
    ht = HashTable(size=2)
    ht.set('name', 'John')
    ht.set('age', 30)
    ht.set('city', 'New York')
    assert ht.get('name') == 'John'
    assert ht.get('age') == 30
    assert ht.get('city') == 'New York'

def test_collision_retrieval():
    ht = HashTable(size=2)
    ht.set('name', 'John')
    ht.set('age', 30)
    ht.set('city', 'New York')
    assert ht.get('age') == 30

def test_hash_in_range():
    ht = HashTable(size=1024)
    key = 'test_key'
    hashed_index = ht._HashTable__hash(key)
    assert 0 <= hashed_index < 1024

