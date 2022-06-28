# ============================  __str__, __repr__, __len__, __abs__  ============================
class Cat:
    def __init__(self, name):
        self.name = name

    # cat отладка
    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    # print(cat) str(cat) для пользователя
    def __str__(self):
        return f'{self.name}'


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, 2, -3, -4)
print(len(p))
print(abs(p))
cat = Cat('vasia')
print(cat)