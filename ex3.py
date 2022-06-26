# ======================================= ИНИЦИАЛИЗАТОР и ФИНАЛИЗАТОР =======================================
class Point:
    # Создание
    def __init__(self, x=0, y=0):
        print('INIT')
        self.x = x
        self.y = y

    def __del__(self):
        print('deleted - ' + str(self))


y = Point()
x = Point(1, 10)
print(x.__dict__)
print(y.__dict__)
print(x.x, x.y)

