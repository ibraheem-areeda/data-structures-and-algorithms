class Tnode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, value, right=None, left=None):
        """
        Initializes a tree node with the given value and optional left and right child nodes.

        Args:
            value: The value of the node.
            right: The right child node (default: None).
            left: The left child node (default: None).
        """
        self.value = value
        self.right = right
        self.left = left

    # def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            A string representation of the node.
        """
        # if self.value is None:
        #     return "This tree node is empty"

        # if self.right.value is None:
        #     return "This node's right child is empty"

        # if self.left.value is None:
        #     return "This node's left child is empty"

        # return f"The tree node value = {self.value}, its left node value = {self.left.value}, its right node value = {self.right.value}"

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


class Tree:
    """
    Represents a binary tree.
    """

    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def __str__(self):
        """
        Returns a string representation of the tree.

        Returns:
            A string representation of the tree.
        """
        if self.root is None:
            return "this Tree is empty"
        return f"the Tree root = {self.root.value},"

    def breadth_first(self):
        """
        Performs a breadth-first traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the breadth-first traversal order.
        """
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        """
        Performs a pre-order traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the pre-order traversal order.
        """
        output = []

        def _walk(root):
            output.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        """
        Performs an in-order traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the in-order traversal order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            output.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self):
        """
        Performs a post-order traversal of the tree and returns a list of node values in the traversal order.

        Returns:
            A list of node values in the post-order traversal order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            output.append(root.value)

        _walk(self.root)
        return output
    
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
  
  def delete(self, key):
        '''
        Delete the key and its associated value from the hashtable
        arg: key
        Returns: None
        '''
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            prev = None
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    if prev is None:
                        bucket.head = curr.next
                    else:
                        prev.next = curr.next
                    self.keys.remove(key)
                    return
                prev = curr
                curr = curr.next

  def update(self, key, new_value):
      '''
      Update the value associated with the given key in the hash table.
      If the key does not exist, this method does nothing.
      Args:
      key: The key for which the value needs to be updated.
      new_value: The new value to be associated with the key.
      Returns: None
      '''
      index = self.__hash(key)
      bucket = self.__buckets[index]
      if bucket is not None:
          curr = bucket.head
          while curr:
              if curr.value[0] == key:
                  curr.value[1] = new_value
                  return
              curr = curr.next

class Binary_Search_Tree(Tree):
    """
    Represents a binary search tree, which is a specialized version of a binary tree.
    """

    def __init__(self, root=None):
        """
        Initializes a binary search tree with the given root.

        Args:
            root: The root node of the binary search tree (default: None).
        """
        self.root = root

    def __str__(self):
        """
        Returns a string representation of the binary search tree.

        Returns:
            A string representation of the binary search tree.
        """
        if self.root is None:
            return "This binary tree is empty"

        return f"The tree root = {self.root.value}"

    def add(self, value):
        """
        Adds a node with the given value to the binary search tree.

        Args:
            value: The value of the node to be added.
        """
        tn_value = Tnode(value)

        def _walk(root):
            
            if root.value <= tn_value.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = Tnode(value)

            if root.value > tn_value.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = Tnode(value)

        _walk(self.root)

    def contains(self, value):
        """
        Checks if the binary search tree contains a node with the given value.

        Args:
            value: The value to search for in the binary search tree.

        Returns:
            True if the binary search tree contains a node with the given value, False otherwise.
        """

        def _walk(root):
            
            if root is None :
                return False

            if root.value == value:
                return True
        
            if root.value < value:
                return _walk(root.right)

            if root.value > value:
                return _walk(root.left)

        return _walk(self.root)

def tree_intersection(tree1, tree2):
    """
    Find the intersection of values between two binary trees.
    
    Parameters:
        tree1 (BinaryTree): The first binary tree.
        tree2 (BinaryTree): The second binary tree.

    Returns:
        list: A list containing the values that are common to both trees
    """
    
    hasht = HashTable()

    def save (node):
        if node:
            hasht.set(str(node.value), 1)
            save (node.left)
            save (node.right)
    save (tree1.root)

    intersection = []

    def check_saved (node):
        if node:
            if hasht.has(str(node.value)) :
                if node.value not in intersection:
                    intersection.append(node.value)
            check_saved (node.left)
            check_saved (node.right)
    check_saved (tree2.root)

    return intersection
  
if __name__ =="__main__":
    
    hashtable = HashTable()
    hashtable.set("key1", "value1")
    # print(hashtable.keys())

    
    l = Tnode(81)
    r = Tnode(20)
    tn1 = Tnode(10,r,l)
    t1 = Binary_Search_Tree(tn1)
    t1.add(7)
    t1.add(9)
    t1.add(15)
    t1.add(40)

    l2 = Tnode(8)
    r2 = Tnode(20)
    tn2 = Tnode(10,r,l)
    t2 = Binary_Search_Tree(tn1)
    t2.add(7)
    t2.add(9)
    t2.add(15)
    t2.add(30)



    print(tree_intersection(t1,t1))


