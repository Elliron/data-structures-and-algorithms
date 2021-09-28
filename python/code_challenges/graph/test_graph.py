from graphs import *
import pytest

def test_vertex():
    node = Vertex("apple")
    assert node.value == "apple"

def test_vertex_not():
    node = Vertex("apple")
    assert node.value != "apple pie"

def test_edge():
    edgie = Edge("apple", "banana")
    assert edgie.vertex == "apple"

def test_edge_not():
    edgie = Edge("apple", "banana")
    assert edgie.vertex != "apple pie"

def test_graph():
    g = Graph()
    g.add_node("apple")
    g.add_node("pear")
    assert g.size() == 2

def test_graph_not():
    g = Graph()
    g.add_node("apple")
    g.add_node("pear")
    assert g.size() != 3
