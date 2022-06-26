# ======================================= МЕТОДЫ КЛАССОВ (self) =======================================
class Point:
    color = 'red'
    circle = 2

    # Параметр self является ссылкой на экземпляр класса
    def set_coords(self):
        print('Set coordinate method' + str(self))  # + адрес объекта


pt = Point()
print(pt.set_coords)
pt.set_coords()
Point.set_coords(pt)


class PointTwo:

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = PointTwo()
pt2 = PointTwo()
pt2.set_coords(10, 29)
pt.set_coords(1, 2)

print(pt.__dict__)
print(pt2.__dict__)

# Имена методов в классах это те же самые атрибуты, только ведут не на данные, а на функции
print(pt.get_coords())
f = getattr(pt, 'get_coords')
print(f())