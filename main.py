import argparse
import kruskal
import prim
import dijkstra


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('input', default='', help='Input file path.')
    argparser.add_argument('-k', '--kruskal', action='store_true', help='Run Kruskal\'s minimum spanning tree algorithm.')
    argparser.add_argument('-p', '--prim', action='store_true', help='Run Prim\'s minimum spanning tree algorithm.')
    argparser.add_argument('-d', '--dijkstra', action='store_true', help='Run Dijkstra\'s shortest path algorithm.')

    args, _ = argparser.parse_known_args()

    if args.kruskal:
        kruskal.minimum_spanning_tree(args.input)
    elif args.prim:
        prim.minimum_spanning_tree(args.input)
    elif args.dijkstra:
        dijkstra.shortest_path(args.input)


if __name__ == '__main__':
    main()
