class Edge:

    def __init__(self, weight, v1_int, v2_int):
        self.weight = weight
        self.vert_pair = [v1_int, v2_int]

    def __repr__(self):
        return f'weight: {self.weight}\tvertices: {self.vert_pair}'
