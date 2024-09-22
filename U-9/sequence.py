# Задание No3
# Во входную строку вводится последовательность чисел через пробел. Для
# каждого числа выведите слово ”YES” (в отдельной строке), если это число
# ранее встречалось в последовательности или ”NO”, если не встречалось.
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-9/sequence.py
#

print()
print('--- Последовательность чисел ---')
print()

num_list = list()

num_list = input('Введите последовательность чисел через пробел: ').split()

print('Введённая последовательность: ',num_list)

for num in range(len(num_list)):
    if num_list[num] in num_list[:num]:
        print('Yes', ' - ', num_list[num])
    else:
        print ('No')