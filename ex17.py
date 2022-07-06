# ==================== ФУНКУИЯ bool() и магические методы ========================

# __len__() - вызывается функцией bool() если не определен магический метод __bool__

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print('__bool__')
        return self.x == self.y



p = Point(3, 3)
print(len(p))
print(bool(p))