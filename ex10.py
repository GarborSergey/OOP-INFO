# ============================ Пример использования объектов property  ============================
from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзиклмнопрстуфкхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.varify_fio(fio)
        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def varify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('fio must be string!')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('invalid format fio')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('in fio must be 1 or more chars')
            if len(s.strip(letters)) != 0:
                raise TypeError('in fio ABS error')

    @classmethod
    def varify_old(cls, old):
        if type(old) != int or 14 > old or old > 120:
            raise TypeError('old must be int type in range (14, 200)')

    @classmethod
    def varify_weight(cls, weight):
        if type(weight) != float or 20 > weight:
            raise TypeError('weight must be float type more than 20')

    @classmethod
    def varify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('ps must be string')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('invalid ps format')

        for p in s:
            if not p.isdigit():
                raise TypeError('ps must be intenger str')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.varify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.varify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.varify_ps(ps)
        self.__passport = ps








p = Person('baba sasa yol', 30, '1234 567890', 20.0)
print(p.fio)
print(p.old)
print(p.weight)
print(p.passport)
p.old = 1200