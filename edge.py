"""Edges used on Kruskal, Prim and Dijkstra algorithms. One edge have its
 value (weight) and a pair of vertices.

Dev: Caio Moraes
GitHub: MoraesCaio
Email: caiomoraes.cesar@gmail.com
"""
from vertex import Vertex


class Edge:

    """
    Attributes:
        vert_pair (list): Pair of vertices
        weight (int): Edge value
    """

    def __init__(self, weight, vertex1, vertex2):
        """Edge constructor

        Args:
            weight (int): Edge value
            vertex1 (Vertex): One of the edge's vertices
            vertex2 (Vertex): One of the edge's vertices
        """
        self.weight = weight
        self.vert_pair = [vertex1, vertex2]

    def __str__(self):
        """Edge string representation

        Returns:
            str: Formatted string
        """
        return f'weight: {self.weight}  \tvertices: {self.vert_pair}'

    def get_other_vertex_idx(self, vert):
        """Get the other vertex index using one of
         the vertices.

        Args:
            vert (Vertex | int): The already known vertex of the edge

        Returns:
            int: -1, if 'vert' is not on the edge
                 0|1, the other vertex's key
        """
        vert = vert.key if type(vert) == Vertex else vert

        for i, v in enumerate(self.vert_pair):
            if v.key == vert:
                return (i + 1) % 2
        return -1

    def get_other_vertex(self, vert):
        """Get the other vertex using one of the vertices.

        Args:
            vert (Vertex | int): The already known vertex of the edge

        Returns:
            Vertex: The other vertex of the edge
        """
        vert = vert.key if type(vert) == Vertex else vert
        return self.vert_pair[self.get_other_vertex_idx(vert)]
