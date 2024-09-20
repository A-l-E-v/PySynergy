# Задание No3
# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали,
# что минимальная сумма инвестиций - X долларов, больше инвестировать
# можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба
# могут вложиться - выведите 2, если только Майкл - Mike, если только Иван -
# Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-5/invest.py
#

print()
print('--- Майкл и Иван ---')
print()

minX=float(input('Введите минимальную сумму инвестиций Х: '))
MikeA=float(input('Сколько долларов у Майкла? '))
IvanB=float(input('Сколько долларов у Ивана? '))

if MikeA>=minX and IvanB>=minX:
    print('2')
    exit(0)
if MikeA>=minX and IvanB<minX:
    print('Mike')
    exit(0)
if MikeA<minX and IvanB>=minX:
    print('Ivan')
    exit(0)
if MikeA+IvanB>=minX:
    print('1') 
else:
    print('0')