# ==================== НАСЛЕДОВАНИЕ НАЧАЛО =======================

class Geom:
    name = 'Geom'

    def set_coords(self, x, y):  # Параметр self может ссылаться на объекты дочерних классов
        self.x = x
        self.y = y
        self.draw()

    def draw(self):
        print('Drawing primitive!')


class Line(Geom):
    def draw(self):
        print('Drawing line!')


class Rect(Geom):
    def draw(self):
        print('Drawing rectangle!')


l = Line()
r = Rect()
g = Geom()

g.set_coords(1, 0)
l.set_coords(1, 1)
r.set_coords(1, 1)


print(l.__dict__)
print(r.__dict__)
