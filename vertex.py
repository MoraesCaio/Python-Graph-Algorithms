from sys import maxsize


class Vertex:

    def __init__(self, key, value=maxsize, parent_key=-1):
        self.key = key
        self.value = value
        self.parent_key = parent_key

    def __repr__(self):
        value = 'MAX_VAL' if self.value == maxsize else self.value
        parent_key = 'NULL' if self.parent_key == -1 else self.parent_key
        return f'{{{self.key}: val={value}, \t par_key={parent_key}}}'
