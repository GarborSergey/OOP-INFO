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

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('right operand must be int or Clock')

        return other if isinstance(other, int) else other.seconds

    def __sub__(self, other):
        return Clock(self.seconds - self.__verify_data(other))

    def __mul__(self, other):
        return Clock(self.seconds * self.__verify_data(other))

    def __truediv__(self, other):
        return Clock(self.seconds // self.__verify_data(other))

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
t1 = Clock(3000)
t2 = Clock(3000)
t += t1 + t2
t += 100
print(t.get_time())
x = t1 - t2
print(x.get_time())
x = t1 * t2
print(x.get_time())
x = t1 / t2
print(x.get_time())