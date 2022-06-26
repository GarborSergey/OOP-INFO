# ======================================= МЕТОД __new__ =======================================
# __new__ вызывается перед созданием класса объекта
# __init__ вызывается сразу после создания объекта класса

# все классы неявно наследуются от класса object
class Point:
    # cls ссылается на класс
    # запускает процесс создание экземпляра
    def __new__(cls, *args, **kwargs):
        print('вызов new для ' + str(cls))
        return super().__new__(cls)  # если убрать будет None

    def __init__(self, x=0, y=0):
        print('init ')
        self.x = x
        self.y = y

# Экз класса не был создан
pt = Point(1, 2)
print(pt)

# паттерн singleton (можно создать только один экземпляр класса)

class Database:
    # =======================================
    __instance = None

    # переопределить метод __call__ еще надо

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Database.__instance = None

    # =======================================

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединения с БД:{self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'данные из БД'

    def write(self, data):
        print(f'запись в БД {data}')



