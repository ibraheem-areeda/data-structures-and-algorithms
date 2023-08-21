# Challenge Title : graph
Implement a graph Class with the following methods:
 - add_vertix
 - add_edge
 - get_vertices
 - size
 - get_neighbors
 - breadth_first

## Whiteboard Process
no Whiteboard requiered

## Approach & Efficiency
the time and space complexities for each of the methods in the graph class:

1. **add_vertix**
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Explanation: Adding a vertex involves creating a Vertix object and adding it to the adjacency list, which is a dictionary. Both operations are constant time operations.

2. **add_edge**
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Explanation: Adding an edge involves appending an Edge object to the adjacency list of two vertices. This operation is constant time as well since dictionaries are used for the adjacency list.

3. **get_vertices**
   - Time Complexity: O(V), where V is the number of vertices
   - Space Complexity: O(V)
   - Explanation: The method simply returns the keys (vertices) of the adjacency list dictionary. The time complexity is linear in the number of vertices since it involves iterating over all vertices.

4. **size**
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   - Explanation: The method directly returns the length of the adjacency list, which is stored as a property of the graph object. Therefore, it's a constant time operation.

5. **get_neighbors**
   - Time Complexity: O(1) on average (amortized), but O(E) in worst case, where E is the number of edges
   - Space Complexity: O(E), where E is the number of edges
   - Explanation: In average cases, looking up neighbors for a given vertex in the adjacency list dictionary is a constant time operation. However, in the worst case, where a vertex has a large number of neighbors, the time complexity becomes proportional to the number of neighbors (edges) connected to that vertex.

6. **breadth_first**
   - Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
   - Space Complexity: O(V), where V is the number of vertices (for the visited set and the queue)
   - Explanation: The breadth-first traversal visits all vertices and edges in the graph. Each vertex is enqueued and dequeued once, leading to a total of O(V) operations. The exploration of edges depends on the number of edges connected to each vertex, and in the worst case, the total number of edges might be traversed, contributing to the O(E) term in the time complexity.

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

