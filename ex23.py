# ==================== НАСЛЕДОВАНИЕ - РЕЖИМ ДОСТУПА  =======================

class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return (self.__x1, self.__y1)


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill):
        super().__init__(x1, x2, y1, y2)
        self.__fill = fill

    # def get_coords(self):
    #     return (self.__x1, self.__y1)  # ОШИБКА 'Rect' object has no attribute '_Rect__x1'


r = Rect(0, 0, 10, 20, 'red')
print(r.get_coords())
print(r.__dict__)  # ссылки на атрибуты '_Geom__x2': 0 ... - особенность поведения
