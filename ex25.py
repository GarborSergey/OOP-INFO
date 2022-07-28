# ============================== МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ =======================================

class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1)
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self, p1):
        print('init MixinLog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: item was sold in 00:00')

    def print_info(self):
        print('print info in MixinLog!!')


class MixinLog2:
    def __init__(self, p1, p2):  # Лучше избегать задание параметров здесь
        super().__init__(1, 2)
        print('init MixinLog2')


class NoteBook(Goods, MixinLog, MixinLog2):
    pass

    # def print_info(self):
    #     MixinLog.print_info(self)


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)  # MRO - Method Resolution Order
MixinLog.print_info(n)  # Можно переопределить в классе
