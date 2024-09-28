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

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"