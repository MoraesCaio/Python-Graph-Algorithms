"""Python Kruskal's algorithm implementation. Constructs a minimum spanning tree
 from a source vertex (node). The sum of the MST edges values are the
 minimum possible.

Dev: Caio Moraes
GitHub: MoraesCaio
Email: caiomoraes.cesar@gmail.com
"""
from utils import parse_file


def minimum_spanning_tree(input='', starting_vert=0, verbose=True):
    """Parse the input file (utils.parse_file) and runs the algorithm using
     the edges and the vertices obtained from parsing. Returns the edges list
     of a minimum spanning tree (there may be multiples MST).

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
        print('#### CHOSEN EDGES ####')
        for e in chosen_edges:
            print(f'Weight: {e.weight}  \tVertices: {e.vert_pair[0].key}-{e.vert_pair[1].key}')

    return chosen_edges
