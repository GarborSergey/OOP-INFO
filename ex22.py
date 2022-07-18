# ==================== ф-ия super() =======================
# Расширение и переопределение

class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'Initialization Geom for {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Drawing line!')


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        # Geom.__init__(self, x1, x2, y1, y2) Явное указание
        super().__init__(x1, x2, y1, y2)
        print('Initialization Rect')
        self.fill = fill


l = Line(0, 1, 1, 1)
r = Rect(1, 1, 1, 1, 1)
print(l.__dict__)
print(r.__dict__)