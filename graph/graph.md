# Challenge Title : hashtable
Implement a graph Class with the following methods:
 - add_vertix
 - add_edge
 - get_vertices
 - size
 - breadth_first

## Whiteboard Process
no Whiteboard requiered

## Approach & Efficiency
the time and space complexities for each of the methods in the graph class:

1. `add_vertex`:
   - Time Complexity: O(1)
     This method involves creating a new Vertex object and adding an empty list to the adjacency list. Both of these operations take constant time.

   - Space Complexity: O(1)
     The additional space used is proportional to the new vertex and the empty list added to the adjacency list. Since the amount of memory used is constant regardless of the size of the graph, the space complexity is constant.

2. `add_edge`:
   - Time Complexity: O(1)
     The time complexity of adding an edge is constant since it involves appending elements to lists (adjacency lists) for the two vertices.

   - Space Complexity: O(1)
     Similar to the `add_vertex` method, the space complexity is constant because it involves adding references to edge objects in the adjacency lists.

3. `get_vertices`:
   - Time Complexity: O(V), where V is the number of vertices.
     The method iterates through the keys of the adjacency list, which represent the vertices. In the worst case, it has to iterate through all vertices, resulting in a linear time complexity.

   - Space Complexity: O(V)
     The space complexity is proportional to the number of vertices because it returns a collection containing all vertices.

4. `size`:
   - Time Complexity: O(1)
     The size of the graph is stored internally as the length of the adjacency list. Retrieving this value is a constant-time operation.

   - Space Complexity: O(1)
     The space complexity is constant since it involves storing a single integer value representing the size of the graph.

5. `breadth_first`:
   - Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
     In the worst case, each vertex and edge will be visited once. Visiting each vertex takes constant time, and visiting each edge is also constant time due to the nature of adjacency lists.

   - Space Complexity: O(V)
     The space complexity is determined by the additional data structures used during the breadth-first traversal, namely the queue and the visited set. In the worst case, all vertices are enqueued in the queue (V elements) and stored in the visited set (V elements). Therefore, the space complexity is proportional to the number of vertices.

## Solution
```
from collections import deque 

class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)



class Vertix:

    def __init__(self, value):

        self.value = value

    def __str__(self):
        return self.value


class Edge:

    def __init__(self, vertix, weight=0):
        self.weight = weight
        self.vertix = vertix

class Graph:

    def __init__(self):
        self.__adj_list = {}
      
    def add_vertix(self,value):
      '''
      Arguments: value
      Returns: The added vertex
      Add a vertex to the graph
      '''
  
      vertix = Vertix(value)
      self.__adj_list[vertix] = []
      return vertix

  

    def add_edge(self, start_vertix, end_vertix, weight=0):
        '''
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''
        if start_vertix not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertix not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertix, weight)
        edge2 = Edge(start_vertix)
        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)

  
  
    def get_vertices(self):
      '''
        Arguments: none
        Returns all of the vertices in the graph as a  
        collection (set, list, or similar)
        Empty collection returned if there are no vertices
      '''
  
      return self.__adj_list.keys()

  
    def size(self):
      return len(self.__adj_list)
  
    def get_neighbors(self,vertix):
      '''
      get neighbors
      A rguments: vertex
      Returns a collection of edges connected to the 
      given vertex
      Include the weight of the connection in the returned collection
      Empty collection returned if there are no vertices
      '''
      
      return self.__adj_list.get(vertix, [])
  
    def breadth_first(self,start_vertix):
    
        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertix)
        visted.add(start_vertix)

        while len(q):
            current_vertix = q.dequeue()

            result.append(current_vertix.value)

            neighbors =self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result
```

