"""Common functions for this module.

Dev: Caio Moraes
GitHub: MoraesCaio
Email: caiomoraes.cesar@gmail.com
"""
from edge import Edge
from vertex import Vertex
import math


def parse_file(file, verbose=True):
    """Parse text file. Expected format:
    '{vertices_number_on_first_line}
     {AB} {AC} .... .... {AZ}
     {BC} {BD} .... {BZ}
     ....
     {YZ}
    '
    If the edge does not exist, its value on the file can be an invalid
     can be informed as an letter.

    Args:
        file (str): Input file path
        verbose (bool, optional): Whether, or not, it should print parsed edges

    Returns:
        tuple(list, list): Tuple containing vertices list and edges list
    """

    #   First line contains the vertices number (not used)
    #   The rest of the lines is a superior triangular matrix without identity diagonal
    edges = []

    with open(file, 'r') as f:

        # First line
        vertices = [Vertex(i) for i in range(int(f.readline()))]

        for i, line in enumerate(f):

            line_weights = line.split()

            for j, weight in enumerate(line_weights):
                try:
                    value = int(weight)
                except ValueError as e:
                    pass
                else:
                    edges.append(Edge(value, vertices[i], vertices[i + j + 1]))

    print('\n#### EDGES ####', *edges, sep='\n')

    return vertices, edges


def search_vertex_edges(edges, vertex_key, excluded_verts=[]):
    """Search for every edge on 'edges', that contains the vertex with
     'vertex_key' but does not contain any of the 'excluded_verts'.

    Args:
        edges (list): List of edges to search on
        vertex_key (int): Key of the vertex to be searched
        excluded_verts (list, optional): Keys of the vertices to disconsider

    Returns:
        list: Found edges
    """
    excluded_verts_keys = [v.key for v in excluded_verts]
    found = []

    for edge in edges:

        if vertex_key in [edge.vert_pair[0].key, edge.vert_pair[1].key]:

            other_vertex_key = edge.get_other_vertex(vertex_key).key

            if other_vertex_key not in excluded_verts_keys:
                found.append(edge)

    return found


# HEAP FUNCTIONS
def _parent(i):
    """Get parent vertex index

    Args:
        i (int): Vertex index

    Returns:
        int: Parent vertex index
    """
    return math.ceil(i / 2) - 1


def _left(i):
    """Get left child vertex index

    Args:
        i (int): Vertex index

    Returns:
        int: Left child vertex index
    """
    return i * 2 + 1


def _right(i):
    """Summary

    Args:
        i (int): Vertex index

    Returns:
        int: Right child vertex index
    """
    return i * 2 + 2


def min_heapify(seq, heap_last_idx=-1):
    """Rearrange the list (used as an heap tree/priority queue)
     placing the edge with lowest value on the root (index 0).

    Args:
        seq (list): Edges list
        heap_last_idx (int, optional): (legacy) Last index of the heap
         on the list
    """

    heap_last_idx = len(seq) - 1 if heap_last_idx == -1 else heap_last_idx
    starting_idx = _parent(heap_last_idx)

    for i in range(starting_idx, -1, -1):

        L = _left(i)
        R = _right(i)

        min_val = i

        if L <= heap_last_idx and seq[L].value < seq[min_val].value:
            min_val = L
        if R <= heap_last_idx and seq[R].value < seq[min_val].value:
            min_val = R

        seq[i], seq[min_val] = seq[min_val], seq[i]
