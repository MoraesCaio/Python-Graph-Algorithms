from edge import Edge
from vertex import Vertex


def _parse_file(file, verbose=True):
    #   First line contains the vertices number (not used)
    #   The rest of the lines is a superior triangular matrix without identity diagonal
    edges = []

    with open(file, 'r') as f:

        # First line
        vertices = [Vertex(i) for i in range(int(f.readline()))]

        for i, line in enumerate(f):

            line_weights = line.split()

            for j, weight in enumerate(line_weights):
                edges.append(Edge(int(weight), vertices[i], vertices[i + j + 1]))

    print('\n#### EDGES ####', *edges, sep='\n')

    return vertices, edges
