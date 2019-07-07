"""Vertices used on Kruskal, Prim and Dijkstra algorithms. One vertex have its
 index (key), its value (for Prim and Dijkstra) and its
 parent index (parent_key).

Dev: Caio Moraes
GitHub: MoraesCaio
Email: caiomoraes.cesar@gmail.com
"""
from sys import maxsize


class Vertex:

    """
    Attributes:
        key (int): Index of the vertex
        value (int): Value of the vertex (for Prim and Dijkstra)
        parent_key (int): Index of parent vertex
    """

    def __init__(self, key, value=maxsize, parent_key=-1):
        """Vertex constructor

        Args:
            key (int): Index of the vertex
            value (int, optional): Value of the vertex (for Prim and Dijkstra)
            parent_key (int, optional): Index of parent vertex
        """
        self.key = key
        self.value = value
        self.parent_key = parent_key

    def __repr__(self):
        """Vertex string representation

        Returns:
            str: Formatted string
        """
        value = 'MAX_VAL' if self.value == maxsize else self.value
        parent_key = 'NULL' if self.parent_key == -1 else self.parent_key
        return f'{{{self.key}: Value={value}, \t Parent Key={parent_key}}}'
