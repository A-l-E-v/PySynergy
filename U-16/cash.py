# Задание No1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у
# него есть методы:
# ● top_up(X) - пополнить на X
# ● count_1000() - выводит сколько целых тысяч осталось в кассе
# ● take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не
# достаточно денег
# 
# https://github.com/A-l-E-v/PySynergy/blob/main/U-16/cash.py
#

# функция печати тысяч в кассах и точных сумм
def total():
    print (f'В кассе 0 сейчас {Kassa0.count_1000()} тысяч, точная сумма: {Kassa0.amount}.')
    print (f'В кассе 1 сейчас {Kassa1.count_1000()} тысяч, точная сумма: {Kassa1.amount}.')
    print (f'В кассе 2 сейчас {Kassa2.count_1000()} тысяч, точная сумма: {Kassa2.amount}.')
    print()

# пустой класс ошибки
class NotEnoughMoney(ValueError):
    pass

class Kassa():

# инициализация начального баланса
    def __init__ (self, amount=0):
        self.amount = amount

# пополнение на X 
    def top_up(self,X):
        self.amount += X

# пересчёт тысяч в кассе
    def count_1000(self):
        return self.amount//1000

# выдача суммы X
    def take_away(self,X):
        if self.amount >= X:
            self.amount -=X
        else:
            # return False
            # поднимаем ошибку изъятия денег
            raise ValueError(NotEnoughMoney) 


# проверим работу трёх касс
Kassa0 = Kassa()            # пустая касса
Kassa1 = Kassa (150000)
Kassa2 = Kassa (7500000)

total()

# пополним три кассы на 1 тыс
Kassa0.top_up(1000)
Kassa1.top_up(1000)
Kassa2.top_up(1000)

total()

# пробуем снять по 2 тысячи из каждой кассы
try:
    Kassa0.take_away(2000)
except ValueError:
    print ('В кассе 0 недостаточно денег.')
    print()

try:
    Kassa1.take_away(2000)
except ValueError:
    print ('В кассе 1 недостаточно денег.')
    print()


try:
    Kassa2.take_away(2000)
except ValueError:
    print ('В кассе 2 недостаточно денег.')
    print()

total()