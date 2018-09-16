import argparse


class Edge:
    weight = 0

    def __init__(self, weight, v1_int, v2_int):
        self.weight = weight
        self.vert_pair = []
        self.vert_pair.append(v1_int)
        self.vert_pair.append(v2_int)

    def __repr__(self):
        return f'weight: {self.weight}\tvertices: {self.vert_pair}'


def main():
    edges = []
    chosen_edges = []

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', default='', help='Input file path.')

    args, _ = argparser.parse_known_args()

    # PARSING FILE
    #   First line contains the vertices number (not used)
    #   The rest of the lines is a superior triangular matrix without identity diagonal
    num_vert = 0
    with open(args.input, 'r') as f:
        num_vert = int(f.readline())
        for i, line in enumerate(f):
            line_weights = line.split()
            for j, val in enumerate(line_weights):
                edges.append(Edge(int(val), i, i+j+1))

    print('#### EDGES ####', *edges, sep='\n')

    # Forest array used for avoiding cyclic trees
    forests = [i for i in range(num_vert)]
    print('\nForest array: ', forests)

    # Kruskal algorithm's
    sorted_edges = sorted(edges, key=lambda x: x.weight)
    print('#### SORTED EDGES ####', *sorted_edges, sep='\n')
    for edge in sorted_edges:
        # If both vertices are not in the same forest
        if not forests[edge.vert_pair[0]] == forests[edge.vert_pair[1]]:
            chosen_edges.append(edge)
            # Unite both forests, updating each one of its vertex's forest index to the first vertex's forest index
            first_forest_val, second_forest_val = forests[edge.vert_pair[0]], forests[edge.vert_pair[1]]
            for i, forest in enumerate(forests):
                if forest in [first_forest_val, second_forest_val]:
                    forests[i] = first_forest_val

    print('\nForest array: ', forests)

    print('#### CHOSEN EDGES ####', *chosen_edges, sep='\n')


if __name__ == '__main__':
    main()
