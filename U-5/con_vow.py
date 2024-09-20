# Задание No2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных
# букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с
# помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из
# перечисленных букв нет - Выведите False
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-5/con_vow.py
#

print()
print('--- Гласные и согласные ---')
print()

word = input ('Введите слово: ').lower()
print ()
print('Анализируем слово: ', word)

vowels = sum(x in 'aeiou' for x in word)
consonants = len(word)-vowels

print ('Гласных: ', vowels)
print ('Согласных: ', consonants)
