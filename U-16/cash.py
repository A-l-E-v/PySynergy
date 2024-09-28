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


class Kassa():

# инициализация начального баланса
    def __init__ (self, amount):
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
            return False


Kassa1 = Kassa (150000)
Kassa2 = Kassa (7500000)

print (f'В кассе 1 сейчас {Kassa1.count_1000()} тысяч.')
print (f'В кассе 2 сейчас {Kassa2.count_1000()} тысяч.')