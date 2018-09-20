from vertex import Vertex


class Edge:

    def __init__(self, weight, vertex1, vertex2):
        self.weight = weight
        self.vert_pair = [vertex1, vertex2]

    def __repr__(self):
        return f'weight: {self.weight}  \tvertices: {self.vert_pair}'

    def get_other_vertex_idx(self, vert):
        vert = vert.key if type(vert) == Vertex else vert

        for i, v in enumerate(self.vert_pair):
            if v.key == vert:
                return (i + 1) % 2
        return -1

    def get_other_vertex(self, vert):
        vert = vert.key if type(vert) == Vertex else vert
        return self.vert_pair[self.get_other_vertex_idx(vert)]
