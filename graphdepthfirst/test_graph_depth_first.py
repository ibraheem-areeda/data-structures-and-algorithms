from graphdepthfirst.graph_depth_first import Graph,Edge,Vertix,Queue
import pytest



def test_1():
    graph = Graph()
    a = graph.add_vertix('A')
    b = graph.add_vertix('B')
    c = graph.add_vertix('C')
    d = graph.add_vertix('D')
    e = graph.add_vertix('E')
    f = graph.add_vertix('F')
    g = graph.add_vertix('G')
    h = graph.add_vertix('H')

    graph.add_edge(a, d)
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(b, d)
    graph.add_edge(b, c)
    graph.add_edge(c, b)
    graph.add_edge(c, g)
    assert graph.breadth_first(a) == ['A', 'D', 'B', 'C', 'G']


def test_2():
    graph = Graph()
    a = graph.add_vertix('A')
    b = graph.add_vertix('B')
    c = graph.add_vertix('C')
    d = graph.add_vertix('D')
    e = graph.add_vertix('E')
    f = graph.add_vertix('F')
    g = graph.add_vertix('G')
    h = graph.add_vertix('H')

    graph.add_edge(a, d)
    graph.add_edge(a, f)
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(c, e)
    graph.add_edge(c, b)
    graph.add_edge(c,h)
    assert graph.breadth_first(a) == ['A', 'D', 'F', 'C', 'E', 'B', 'H']


def test_3():
    graph = Graph()
    a = graph.add_vertix('A')
    b = graph.add_vertix('B')
    c = graph.add_vertix('C')
    d = graph.add_vertix('D')
    e = graph.add_vertix('E')
    f = graph.add_vertix('F')
    g = graph.add_vertix('G')
    h = graph.add_vertix('H')

    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(a, d)
    graph.add_edge(b, d)
    graph.add_edge(d, f)
    graph.add_edge(c, g)
    assert graph.breadth_first(a) == ['A', 'B', 'D', 'C', 'F', 'G']


