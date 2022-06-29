# ============================  __add__, __sub__, __mul__, __truediv__  ============================
# __add__ - сложение
# __sub__ - вычитание
# __mul__ - умножение
# __truediv__ - деление

class Clock:
    __DAY = 86400

    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise TypeError('second must be int')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}'

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('right el must be int or Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print('__iadd__')

        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("!!!!!!!!")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


t = Clock(1000)
t1 = Clock(2000)
t2 = Clock(3000)
t += t1 + t2
t += 100
print(t.get_time())