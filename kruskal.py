def minimum_spanning_tree(num_vert, edges, verbose=True):
    # Forest array used for avoiding cyclic trees
    #  num_vert is always equal to len(edges) + 1
    forests = [i for i in range(num_vert)]

    if verbose:
        print('\nForest array: ', forests)

    chosen_edges = []
    sorted_edges = sorted(edges, key=lambda x: x.weight)

    if verbose:
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

    if verbose:
        print('\nForest array: ', forests)

    return chosen_edges
