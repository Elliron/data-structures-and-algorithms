from typing_extensions import ParamSpecKwargs

class Graph:
    def __init__(self):
        """Adjacency list is a space-efficient way to use a sparsely connected graph,
        Adjacency matrix is used more connected graphs"""
        self._adjacency_list = {}
        self.total = 0

# TODO1: add node
    def add_node(self, value):
        """Takes a value as an argument, returns a node based on that value and adds it to the graph.
        Nodes are Vertices or points of interconnection between two edges"""
        v = Vertex(value)
        self._adjacency_list[v]= []
        self.size()
        return v

# TODO2: add edge
    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Edges are the lines that connect two Nodes/Vertices to each other, may be one way or two way.
        weight shows the cost of going from one vertex to another."""
        if start_vertex not in self._adjacency_list:
            raise KeyError("Starting Vertex not in Graph")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in Grapjh")

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

# TODO3: get nodes
    def get_nodes(self):
        """Returns all of the nodes in the graph as a collection"""
        return self._adjacency_list.keys()


# TODO4: get neighbors
    def get_neighbors(self):
        """Takes nodes as arguments, Returns a collection of edges connected to the given node, including weight"""
        return self._adjacency_list.values()


# TODO5: size
    def size(self):
        """Returns the total number of nodes in the graph"""
        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

