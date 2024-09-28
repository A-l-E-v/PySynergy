# Задание No1
# Есть родительский класс:
# class Transport:
# def __init__(self, name, max_speed, mileage):
# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
# Создайте объект Autobus, который унаследует все переменные и методы
# родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renault Logan Скорость: 180 Пробег: 12
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-15/bus_name.py
#

class Transport:
    # конструктор
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    # метод печати объекта
    def print_me(self):
        return print (f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}' )

# создаём объект
Autobus = Transport ('Renault Logan', 180, 12)

# вызываем метод печати
Autobus.print_me()