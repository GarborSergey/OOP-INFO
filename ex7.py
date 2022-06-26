# =================================== геттеры и сеттреы ===================================

class Point:
    MIN = 0
    MAX = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN <= x <= self.MAX:
            pass

    @classmethod
    def set_bound(cls, left):
        # self.MIN = left  # Так будет присвоено значение экземпляру класса
        cls.MIN = left

    # вызывается при обращении к атрибуту экземпляра класса
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('no dostup')
        return object.__getattribute__(self, item)

    # каждый раз при присвоении атрибуту определенного значения
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('not value')
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value

    # каждый раз при обращении к несуществующему атрибуту экземпляру класса
    def __getattr__(self, item):
        print('__getattr__ - ' + item)
        return False

    # каждый раз когда удаляется определенный атрибут из экз. класса
    def __delattr__(self, item):
        print('__delattr__ - ' + item)
        object.__delattr__(self, item)

pt = Point(1, 2)
a = pt.y
print(pt.yy)
print(pt.y)
pt.yy
pt.y = 10
print(a)
del pt.y
print(pt.__dict__)