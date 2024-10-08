# Задание No1
# Ранее вы выполняли задание связанное с ветеринарной клиникой. В той
# задаче вам предстояло вывести информацию о питомце на экран. Сейчас вам
# необходимо создать словарь pets = {}
# Примерный вид будет следующим:
# pets = {
# "Имя питомца": {
# 'Вид питомца': # придумайте каким образом сюда внести информацию,
# 'Возраст питомца': # придумайте каким образом сюда внести информацию,
# 'Имя владельца': # придумайте каким образом сюда внести информацию
# }
# }
# У вас должен получиться словарь, с ещё одним словарём внутри. То есть, есть
# словарь pets. Он в себе хранит ещё один словарь, который обозначается
# именем питомца. Имя питомца также нужно каким-то образом вносить туда.
# Задача не будет считаться выполненной, если вы заходите сразу внести
# информацию, не прибегая в функции input()
# Например:
# pets = {
# "Мухтар": {
# "Вид питомца": "Собака",
# "Возраст питомца": 9,
# "Имя владельца": "Павел"
# }
# }
# Так должен будет выглядеть результируюший словарь, но первоначальный
# его вид - пустой. Его необходимо заполнить пользовательским вводом через
# консоль с помощью функции input(), а не вписать значения уже в самом коде.
# Возраст питомца должен быть типа int Всё остальное - строкиТак как возраст питомца указывается типом int. 
# Необходимо, в соответствии с
# указанным возрастом выводит год, года или лет. Например:
# Его возраст: 24 года
# Его возраст: 21 год
# Его возраст: 19 лет
# И теперь осталось только получить всю информацию о питомце в виде
# строки, как из задания по Урок No3. Ввод-вывод и базовые переменные. Задание
# No1, но с небольшими изменениями. Для получения информации необходимо
# воспользоваться методами словаря keys() и values():
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца:
# Саша
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-10/pets.py
#


print()
print('--- Информация о питомце ---')
print()

# словарь питомцев
pets = {}

# словарь одного питомца
a_pet =  {}

pet_name = input ('Введите имя питомца: ')
a_pet ['Вид питомца'] = input ('Введите вид питомца: ')
a_pet ['Возраст питомца'] = int(input ('Введите возраст питомца: '))
a_pet ['Имя владельца'] = input ('Введите имя владельца: ')

pets[pet_name] = a_pet

print()
print ('Результирующий словарь: ',pets)
print()

# формируем текст для возраста
year_s = ''
age = pets[pet_name]['Возраст питомца']

if age % 10 == 1 and age != 11 and age % 100 != 11:

    year_s = 'год'

elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:

    year_s = 'года'

else:

    year_s = 'лет'

# Образец строки на вывод:
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
print (f'Это {pets[pet_name]['Вид питомца']} по кличке "{pet_name}". \
Возраст питомца: {pets[pet_name]['Возраст питомца']} {year_s}. \
Имя владельца: {pets[pet_name]['Имя владельца']}')
