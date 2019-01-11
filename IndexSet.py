class IndexSet:

    def __init__(self, size, dim):
        self.dim = dim
        self.size = size
        self.iset = list(range(size - 1, -1, -1))

    def __repr__(self):
        return str(self.iset)

    def __str__(self):
        return str(self.iset)

    def get_sorted_tuple(self):
        r = list(self.iset)
        r.sort()
        return tuple(r)

    def is_no_equals(self):
        return len(set(self.iset)) == self.size

    def is_max(self):
        return all(e == self.dim - 1 for e in self.iset)

    def simple_next(self):
        if not self.is_max():
            self.iset[0] += 1
            for i in range(self.size):
                if self.iset[i] > self.dim - 1:
                    self.iset[i] -= 1
                    self.iset[i] = 0
                    self.iset[i + 1] += 1
            result = True
        else:
            result = False
        return result

    def next(self):
        while True:
            result = self.simple_next()
            if self.is_no_equals() or not result:
                break
        return result


