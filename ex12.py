# ============================ Метод __call__ ============================
import math


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter


c = Counter()  # Когда прописываем круглые скобки после класса акт ивизируется метод call
c()  # Вызываем класс подобно функции, классы которые себя так ведут называются функторы
c(13)
c(100)
c()
c()
res = c()
print(res)
print(c.__dict__)


# Пример использования (вместо замыкания у функции)
class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('arg must be str')

        return args[0].strip(self.__chars)


s1 = StripChars('!&*()')
res = s1('Hello world!!')
print(res)


# Реализация декоратора
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x))/dx


@Derivate
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)  # Применение декоратора

print(df_sin(math.pi/3))