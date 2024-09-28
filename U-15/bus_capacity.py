# Задание No2
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного
# средства:
# class Transport:
# def __init__(self, name, max_speed, mileage):
# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
# def seating_capacity(self, capacity):
# return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renault Logan: 50 пассажиров
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-15/bus_capacity.py
#

# Базовый класс
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# метод базового класса
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):

# если вместимость не передана, то подставляем 50
    def seating_capacity(self, capacity = 50):

        return super ().seating_capacity (capacity)

# испытаем метод родительского класса
tr_test = Transport('Transport test',120,23243)
print (tr_test.seating_capacity(59))

# используя метод дочернего класса, передадим вместимость 76
the_bus = Autobus('The_bus',110,34432)
print(the_bus.seating_capacity(76))
print()

# выполним задание - параметр вместимости не передан, значит будет 50
a_bus = Autobus('Renault Logan',130,54837)
print(a_bus.seating_capacity())


