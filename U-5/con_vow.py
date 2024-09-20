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

# строка гласных букв
letters = 'aeiou'

# ввод слова
word = input ('Введите слово маленькими латинскими буквами: ')


print ()
print('Анализируем слово: ', word)
print()

# считаем сколько гласных
vowels = sum(x in letters for x in word)
# значит, допустим, остальные согласные
consonants = len(word)-vowels

print ('Гласных:   ', vowels)
print ('Согласных: ', consonants)
print()

# считаем a
a=word.count(letters[0])
if a!=0:
    print ('a - ', a)
else: print ('a - FALSE')

# считаем e
e=word.count(letters[1])
if e!=0:
    print ('e - ', e)
else: print ('e - FALSE')

# считаем i
i=word.count(letters[2])
if i!=0:
    print ('i - ', i)
else: print ('i - FALSE')

# считаем o
o=word.count(letters[3])
if o!=0:
    print ('o - ', o)
else: print ('o - FALSE')

# считаем u
u=word.count(letters[4])
if u!=0:
    print ('u - ', u)
else: print ('u - FALSE')
