"""Python Prim's algorithm implementation. Constructs a minimum spanning tree from
 a source vertex (node). Every vertex will have a reference to its parent
 vertex (except the source vertex) thus forming the tree.

Dev: Caio Moraes
GitHub: MoraesCaio
Email: caiomoraes.cesar@gmail.com
"""
from utils import min_heapify
from utils import parse_file
from utils import search_vertex_edges
from utils import print_vertex_tree


def minimum_spanning_tree(input='', starting_vert=0, verbose=True):
    """Parse the input file (utils.parse_file) and runs the algorithm using
     the edges and the vertices obtained from parsing. Returns the modified
     vertices list ('value' and 'parent_key' have new values).

    Args:
        input (str): Input file path (.txt format)
        starting_vert (int, optional): Source vertex key
        verbose (bool, optional): Whether, or not, it should print the result

    Returns:
        list: Chosen edges with new values for 'value' and 'parent_key'

    Raises:
        FileNotFoundError: Raise when input file is not found
    """
    try:
        vertices, edges = parse_file(input, verbose)
    except FileNotFoundError as e:
        raise e

    # settings
    vertices[starting_vert].value = 0
    queue = vertices[:]  # temporary vertex queue list
    chosen_vertices = []

    while len(queue):
        # queue = sorted(queue, key=lambda v: v.value)
        min_heapify(queue)
        vertex = queue.pop(0)
        chosen_vertices.append(vertex)
        next_edges = search_vertex_edges(edges=edges, vertex_key=vertex.key, excluded_verts=chosen_vertices)

        # checking the adjacent new edges
        for edge in next_edges:

            other_vertex = edge.get_other_vertex(vertex.key)

            if edge.weight < other_vertex.value:
                other_vertex.parent_key = vertex.key
                other_vertex.value = edge.weight

    if verbose:
        print_vertex_tree(chosen_vertices)

    return chosen_vertices
