# Задание No2
# Дана строка, длина которой не превосходит 1000. Вам требуется
# преобразовать все идущие подряд пробелы в один. Выведите измененную
# строку.
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-8/spaces.py
#
print ()
print ('--- Объединение пробелов ---')
print ()

# ввод строки с повторяющимися пробелами
text_line = input ('Введите строку с повторяющимися пробелами: ')
res_line = ''

for position in range(len(text_line)):
    # если это буква, то копируем её
    if text_line[position] !=' ':
        res_line+=text_line[position]
    # если это пробел, но до этого была буква, то делаем одиночный пробел
    elif text_line[position-1] != ' ':
        res_line+=' '
    else:
        # при дублировании пробелов не делаем ничего
        continue

print ('Строка без лишних пробелов: ', res_line)
        

