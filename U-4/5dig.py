# Задание No2
# Дано пятизначное целое число. Напишите алгоритм, который возведёт
# количество десятков в степень количества единиц. Затем умножит это число
# на количество сотен. И делит получившееся число на разность количества
# десятков тысяч и количества тысяч
# Например, есть число 46275
# Необходимо возвести 7 (десятки) в степень 5 (единицы), умножить
# получившееся число на 2 (сотни), и разделить на разность между 4 (десятки
# тысяч) и 6 (тысячи) то есть (4-6)
# В результате необходимо получить вещественное число. В нашем примере это
# будет: -16807.0
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-4/5dig.py
#

print()
print('-- Пятизначное число --')
print()
# на всякий случай страхуемся от ввода вещественного числа
number = float(input ('Введите пятизначное целое число: '))
print()
# приводим к целому числу
number = int(number)
print('Введено целое число:       ', number)
print()
#Количество единиц
e=int(float(number%10))
print('Количество единиц:         ',e)
#Количество десятков
d=int(float(number%100)/10)
print('Количество десятков:       ',d)
# Количество сотен
s=int(float(number%1000)/100)
print('Количество сотен:          ',s)
# Количество тысяч
t=int(float(number%10000)/1000)
print('Количество тысяч:          ',t)
# Количество десятков тысяч
dt=int(float(number%100000)/10000)
print('Количество десятков тысяч: ',dt)
print()
print('Алгоритм, который возведёт количество десятков в степень количества единиц.')
print('Затем умножит это число на количество сотен.')
print('И делит получившееся число на разность количества десятков тысяч и количества тысяч')
print('Результат - вещественное число.')
print('Пример: введено 46275, должно получиться: -16807.0')
print()
print('Результат: ', (d**e)*s/(dt-t) )
