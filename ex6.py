# =================================== МЕХАНИЗМ ИНКАПСУЛЯЦИИ ===================================
# механизм ограничения доступа к данным и методам класса извне
# _ - protected (для обращения внутри класса и всем его дочерним классам)
# __ - private (только для обращения внутри класса)
from accessify import private, protected


class Point:
    def __init__(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError(f'coord type must be (int, int) or (float, float) not {(type(x), type(y))}')

    def get_coord(self):
        return self.__x, self.__y


p = Point(1, 2)
p.set_coord(10, 200)
print(p.get_coord())
print(dir(p))
print(p._Point__x)

# pip install accessify
