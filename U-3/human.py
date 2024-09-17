# Задание No2
# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для
# студентов. Он должен запрашивать по порядку этапы развития человека
# (проверим твое умение гуглить, что тоже очень важно для программиста. ) и в
# конце вывести все стадии, разделенные знаком =>, что будет означать
# постепенный переход от одного к другому. В следующих уроках мы дополним
# эту форму до полноценного теста, который будет проверять правильность
# ответов, а пока - начнем с малого. Напоминаем, что разделить эти данные
# тебе поможет команда sep внутри команды print, например, чтобы разделить
# переменные знаком + нужно ввести:
# print(a1, a2, a3, sep='+')
# Подсказка: последняя стадия развития - Homo sapiens sapiens.
#  
#https://github.com/A-l-E-v/PySynergy/blob/main/U-3/human.py
#

print()
print("--- Антропогенез-тест ---")
print()
Stage1 = input ('Введите первый вид (подсказка: Homo habilis): ')
Stage2 = input ('Введите второй вид (подсказка: Homo rudolfensis): ')
Stage3 = input ('Введите третий вид (подсказка: Homo erectus): ')
Stage4 = input ('Введите четвёртый вид (подсказка: Homo georgicus): ')
Stage5 = input ('Введите пятый вид (подсказка: Homo ergaster): ')
Stage6 = input ('Введите шестой вид (подсказка: Homo antecessor): ')
Stage7 = input ('Введите седьмой вид (подсказка: Homo cepranensis): ')
Stage8 = input ('Введите восьмой вид (подсказка: Homo heidelbergensis): ')
Stage9 = input ('Введите девятый вид (подсказка: Homo rhodesiensis): ')
Stage10 = input ('Введите десятый вид (подсказка: Homo neanderthalensis): ')
Stage11 = input ('Введите одиннадцатый вид (подсказка: Homo sapiens sapiens): ')
# Stage12 = input ('Введите двенадцатый вид (подсказка: Homo sapiens idaltu): ')
# Stage13 = input ('Введите тринадцатый вид (подсказка: Homo floresiensis): ')
print(Stage1,Stage2,Stage3,Stage4,Stage5,Stage6,Stage7,Stage8,Stage9,Stage10,Stage11,sep='=>')

