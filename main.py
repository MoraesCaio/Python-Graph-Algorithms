import argparse
from edge import Edge
import kruskal


def main():
    edges = []
    chosen_edges = []

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', default='', help='Input file path.')
    argparser.add_argument('-k', '--kruskal', action='store_true', help='Run Kruskal\'s minimum spanning tree algorithm.')

    args, _ = argparser.parse_known_args()

    # PARSING FILE
    #   First line contains the vertices number (not used)
    #   The rest of the lines is a superior triangular matrix without identity diagonal
    num_vert = 0
    with open(args.input, 'r') as f:
        num_vert = int(f.readline())
        for i, line in enumerate(f):
            line_weights = line.split()
            for j, weight in enumerate(line_weights):
                edges.append(Edge(int(weight), i, i + j + 1))

    print('#### EDGES ####', *edges, sep='\n')

    if args.kruskal:
        chosen_edges = kruskal.minimum_spanning_tree(num_vert, edges)

    print('#### CHOSEN EDGES ####', *chosen_edges, sep='\n')


if __name__ == '__main__':
    main()
