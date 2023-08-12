from graph.graph import Graph,Edge,Vertix,Queue
import pytest

@pytest.fixture
def sample_graph():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    vertex_c = graph.add_vertix('C')
    graph.add_edge(vertex_a, vertex_b, 2)
    graph.add_edge(vertex_b, vertex_c, 3)
    return graph

def test_add_vertex(sample_graph):
    new_vertex = sample_graph.add_vertix('D')
    assert new_vertex in sample_graph.get_vertices()

def test_add_edge(sample_graph):
    vertex_d = sample_graph.add_vertix('D')  
    vertex_e = sample_graph.add_vertix('E') 
    sample_graph.add_edge(vertex_d, vertex_e)
    assert len(sample_graph.get_neighbors(vertex_d)) == 1

def test_get_vertices(sample_graph):
    vertices = sample_graph.get_vertices()
    assert len(vertices) == 3
    assert all(isinstance(vertex, Vertix) for vertex in vertices)

def test_get_neighbors():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    vertex_c = graph.add_vertix('C')
    graph.add_edge(vertex_a, vertex_b, 2)
    graph.add_edge(vertex_b, vertex_c, 3)
    
    neighbors = graph.get_neighbors(vertex_b)
    assert len(neighbors) == 2

def test_neighbors_with_weight(sample_graph):
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    vertex_c = graph.add_vertix('C')
    graph.add_edge(vertex_a, vertex_b, 2)
    graph.add_edge(vertex_b, vertex_c, 3)
    neighbors = graph.get_neighbors(vertex_b)
    assert neighbors[1].weight == 3

def test_graph_size(sample_graph):
    assert sample_graph.size() == 3

def test_single_vertex_edge():
    graph = Graph()
    vertex = graph.add_vertix('A')
    assert graph.size() == 1
    assert len(graph.get_neighbors(vertex)) == 0

