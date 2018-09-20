from utils import _parse_file


def minimum_spanning_tree(input='', vertices=[], edges=[], verbose=True):

    if input != '':
        vertices, edges = _parse_file(input, verbose)
    elif vertices == [] or edges == []:
        raise ValueError('Missing number of vertices and/or edges list.')

    # Forest array used for avoiding cyclic trees
    forests = [i for i in range(len(vertices))]
    chosen_edges = []
    sorted_edges = sorted(edges, key=lambda x: x.weight)

    if verbose:
        print('\nForest array: ', forests, end='\n\n')
        print('#### SORTED EDGES ####', *sorted_edges, sep='\n')

    for edge in sorted_edges:
        # If both vertices are not in the same forest

        if forests[edge.vert_pair[0].key] != forests[edge.vert_pair[1].key]:

            chosen_edges.append(edge)

            # Unite both forests, updating each one of its vertex's forest index to the first vertex's forest index
            first_forest_val  = forests[edge.vert_pair[0].key]
            second_forest_val = forests[edge.vert_pair[1].key]

            for i, forest in enumerate(forests):
                if forest in [first_forest_val, second_forest_val]:
                    forests[i] = first_forest_val

    if verbose:
        print('\nForest array: ', forests, end='\n\n')
        print('#### CHOSEN EDGES ####', *chosen_edges, sep='\n')

    return chosen_edges
