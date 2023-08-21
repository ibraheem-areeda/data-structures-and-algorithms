import pytest
from graph_business_trip.graphbusinesstrip import Graph,Edge,Vertix,Queue,business_trip




def test_from_Metroville_to_Pandora():
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
    graph.add_edge(Naboo, New_Monstropolis, 73)
    graph.add_edge(New_Monstropolis, Arendelle, 42)
    graph.add_edge(Arendelle, pandora, 150)
    total_cost = business_trip(graph,[pandora,Metroville])
    assert total_cost == "$82"

def test_from_Arendelle_to_Naboo():
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
    total_cost = business_trip(graph,arr)
    assert total_cost == "$115"

def test_from_Naboo_to_Pandora():
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
    graph.add_edge(Naboo, New_Monstropolis, 73)
    graph.add_edge(New_Monstropolis, Arendelle, 42)
    graph.add_edge(Arendelle, pandora, 150)
    total_cost = business_trip(graph,[Naboo, pandora])
    assert total_cost == "Null"

def test_from_Narnia_to_Naboo():
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
    graph.add_edge(Naboo, New_Monstropolis, 73)
    graph.add_edge(New_Monstropolis, Arendelle, 42)
    graph.add_edge(Arendelle, pandora, 150)
    total_cost = business_trip(graph,[Narnia, Arendelle, Naboo])
    assert total_cost == "Null"