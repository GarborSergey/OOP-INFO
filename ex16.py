# ============================  __eq__, __hash__ ============================
# ==================== ФУНКУИЯ hash и хэши объектов =======================
# если а == в, то равен их хэш
# равные хэши не гарантируют равенство объектов
# если хэши не равны, то объекты точно не равны

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'[{self.x}, {self.y}]'


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(hash(p1), hash(p2), sep='\n')
print(p1)
d = dict()
d[p1] = 1
d[p2] = 2
print(d)