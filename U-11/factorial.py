# Задание No1
# ● Создайте функцию, которая принимает в качестве параметра -
# натуральное целое число.
# ● Данная функция находит факториал полученного числа
# Например, факториал числа 3 это число 6.
# ● Теперь создайте список факториалов чисел от получившегося ранее
# факториала 6, до 1.
# В итоге, на вход программа получает например число 3, возвращает число 6
# (факториал числа 3) и вам нужно сделать список из факториалов числа 6 в
# убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 -
# это 120 и так далее вплоть до 1
# То есть, результирующий список будет выглядеть в нашем примере так:
# [720, 120, 24, 6, 2, 1]
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-11/factorial.py
#

print()
print('--- Факториалы ---')
print()


# считаем факториал числа рекурсией
def fac(i):
    if i == 1:
        return 1
    return fac(i - 1) * i

number = int (input('От какого числа посчитаем ряд факториалов? '))
# считаем факториал и он будет началом ряда
start = fac(number)
print(f'Факториал: {number}!={start}')

# инициируем список факториалов
fac_list = []

# запускаем цикл от старта до 0 с шагом -1
for series in range(start,0,-1):
    fac_list.append (fac(series))

print ('Список факториалов:', fac_list)