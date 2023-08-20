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

    def __str__(self):
        return str(self.vertix)

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
        
def business_trip(graph, arr_cities):
    cost = 0
    if len(arr_cities) == 0:
        return None
    for city in range(len(arr_cities) - 1):
        for neighbor in graph.get_neighbors(arr_cities[city]):
            if neighbor.vertix == arr_cities[city + 1]:
                cost += neighbor.weight
                print(neighbor)
    if cost == 0:
        return 'Null'
    else:
        return f"${cost}"


if __name__ == "__main__":
    graph = Graph()
    pandora = graph.add_vertix('pandora')
    Metroville = graph.add_vertix('Metroville')
    Narnia = graph.add_vertix('Narnia')
    Arendelle = graph.add_vertix('Arendelle')
    New_Monstropolis = graph.add_vertix('New_Monstropolis')
    Naboo = graph.add_vertix('Naboo')
    graph.add_edge(pandora, Metroville, 82)
    graph.add_edge(pandora, Arendelle, 150)
    graph.add_edge(Metroville, Arendelle, 99)
    graph.add_edge(Metroville, New_Monstropolis, 105)
    graph.add_edge(Metroville, Naboo, 26)
    graph.add_edge(Metroville, Narnia, 37)
    graph.add_edge(Narnia, Naboo, 250)
    graph.add_edge(New_Monstropolis,Naboo, 73)
    graph.add_edge(Arendelle,New_Monstropolis,42)
    graph.add_edge(Arendelle, pandora, 150)
    arr=[Arendelle, New_Monstropolis, Naboo]
    print(business_trip(graph,arr))