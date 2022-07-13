# ==================== ф-ия issubclass() =======================

# Все классы наследуются от базового класса object
class Geom(object):  # Так наследуется неявно!
    pass


class Line(Geom):
    pass


g = Geom()
print(g)
l = Line()

# Проверяет явл-ся ли дочерний(работает с классами, не с экземплярами)
print(issubclass(Line, Geom))
print(issubclass(Geom, Line))


class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


v = Vector([1, 2, 3, 4])
print(v)
