# ============================ Декоратор @property ============================
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    # из каждого экземпляра можем обрашаться к атрибуту age который
    # объект класса property, автоматом вызывает гетер и сетер
    # age = property(get_age, set_age)

    # age = property()
    # age = age.setter(set_age)
    # age = age.getter(get_age)

p = Person('Sergey', 12)
print(p.age )
del p.age
print(p.__dict__)