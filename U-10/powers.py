# Задание No2
# С помощью цикла создайте словарь, в котором ключи будут, например от
# числа 10, до -5 (включительно). А значениями этих ключей будут сами эти
# числа возведённые в степени равных этим числам
# Например:
# my_dict = {
# 10: 10000000000,
# 9: 387420489,
# # и так далее ...
# -5: -0.00032
# }
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-10/powers.py
#

print()
print('--- Степень числа ---')
print()

my_dict={}

for number in range (10,-6,-1):
    my_dict[number] = number ** number

print ('Словарь чисел и их степеней готов! ')
print()
print (my_dict)