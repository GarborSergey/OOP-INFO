# ======================================= АТРИБУТЫ =======================================
class Point:
    color = 'red'
    circle = 2


# Существование атрибута
print(hasattr(Point, 'color'))
print(hasattr(Point, 'not_exist'))

# Получение атрибута
print(getattr(Point, 'circle'))
print(getattr(Point, 'sdsd', 'Not'))  # если не сущ. выводит 3ий арг

# Новый атрибут или изменить значение
setattr(Point, 'prop', 1)
print(Point.__dict__)

a = Point()
a.color = 'green'
# Удаление атрибута(сброс)
del a.color
print(a.color)
