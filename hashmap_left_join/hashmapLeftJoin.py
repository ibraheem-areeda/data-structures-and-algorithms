
class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value

class LinkedList:
    '''
    A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None

    def insert (self, value):
        '''
        insert a new node with the given value at the begining of the linked list.
        args: value
        output : none
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
  '''
  data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    return sum([ord(str(char)) for char in key]) * 283 % self.__size
    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
        ll = LinkedList()
        self.__buckets[index] = ll

    self.__buckets[index].insert([key,value])
    self.keys.append(key)

  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  

  def has(self, key):
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    '''

    if self.get(key):
      return True
    return False  

  def keys(self):
    '''
    args : none
    Returns a list of all the  keys present in the Hashtable.
    '''
    return self.keys
  

def left_join (hashmap1,hashmap2):
    '''
     Perform a left join operation on two hashmaps.

    Args:
        hashmap1 (hash table): The first hashmap.
        hashmap2 (hash table): The second hashmap.

    Returns:
        list: A list of lists with the left join results. Each sublist contains [key, value1, value2],
              where value1 is the corresponding value from hashmap1, and value2 is the corresponding
              value from hashmap2 (or None if the key is not present in hashmap2).
    '''
    record =[]
    for key in hashmap1.keys:
        if hashmap2.has(key):
            record.append([key,hashmap1.get(key),hashmap2.get(key)])
        else:
            record.append([key,hashmap1.get(key),None])
    return record


if __name__ == "__main__":
    hashmap1 = HashTable()
    hashmap2 = HashTable()
    hashmap1.set("good","nice")
    hashmap1.set("cat","kitten")
    hashmap1.set("dog","doggy")
    hashmap2.set("diligent","employed")
    hashmap2.set("guide","usher")
    hashmap2.set("wrath","anger")

    print(left_join(hashmap1,hashmap2))