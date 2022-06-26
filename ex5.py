# =================================== classmethod staticmethod===================================
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # работает с атрибутами класса
    def validate(cls, arg):  # cls ссылка на класс
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod  # не имеет доступ к атрибутам класса не к атрибутам его экземпляра
    def norm2(x, y):
        return x*x + y*y

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y


v = Vector(1, 21)
print(Vector.norm2(5, 6))
print(Vector.validate(10))
print(v.get_coord())