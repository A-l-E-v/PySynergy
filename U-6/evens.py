# Задание No3
# Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные
# числа на заданном отрезке через пробел.
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-6/evens.py
#

print()
print('--- Чётные числа ---')
print()

A=int(input('Введите число А: '))
B=int(input('Введите число B: '))

for number in range (A,B+1):
    if number%2==0: 
        print (str (number),end='')
        print (' ',end='')
print()