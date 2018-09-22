from utils import _parse_file
import math


def _parent(i):
    return math.ceil(i / 2) - 1


def _left(i):
    return i * 2 + 1


def _right(i):
    return i * 2 + 2


def _min_heapify(seq, heap_last_idx=-1):

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


def _search_vertex_edges(edges, vertex_key, excluded_verts=[]):

    excluded_verts_keys = [v.key for v in excluded_verts]
    found = []

    for edge in edges:

        if vertex_key in [edge.vert_pair[0].key, edge.vert_pair[1].key]:

            other_vertex_key = edge.get_other_vertex(vertex_key).key

            if other_vertex_key not in excluded_verts_keys:
                found.append(edge)

    return found


def shortest_path(input='', vertices=[], edges=[], starting_vert=0, verbose=True):

    if input != '':
        vertices, edges = _parse_file(input, verbose)
    elif vertices == [] or edges == []:
        raise ValueError('Missing number of vertices and/or edges list.')

    # settings
    vertices[starting_vert].value = 0
    queue = vertices[:]
    chosen_vertices = []

    while len(queue):
        # queue = sorted(queue, key=lambda v: v.value)
        _min_heapify(queue)
        vertex = queue.pop(0)
        chosen_vertices.append(vertex)
        next_edges = _search_vertex_edges(edges=edges, vertex_key=vertex.key, excluded_verts=chosen_vertices)

        for edge in next_edges:

            path_sum = vertex.value + edge.weight
            other_vertex = edge.get_other_vertex(vertex.key)

            if path_sum < other_vertex.value:
                other_vertex.parent_key = vertex.key
                other_vertex.value = path_sum

    if verbose:
        print('#### CHOSEN EDGES ####', *chosen_vertices, sep='\n')

    return chosen_vertices