# +++++++++++++++++++++++++++ Магический атрибут __slots__ +++++++++++++++++++++++++++

# Для ограничения количества наборов свойств и методов в
# экземпляре применяется специальный магический атрибут __slots__.

class Person:
    __slots__ = ['__name', '__age']

    def __init__(self, name, age):
        self.__name = name
        if self.__name != 'Nikolay':
            self.__name = 'ERROR'
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if self.__name != 'Nikolay':
            self.__name = 'ERROR'

p1 = Person('Ivan', 49)
p2 = Person('Nikolay', 13)
p2.name = 'Serega'
print(p1.name)
print(p2.name)
