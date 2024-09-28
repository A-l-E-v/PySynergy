# Задание No2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также
# s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может
# стать ≤ 0
# ● count_moves(x2, y2) - возвращает минимальное количество действий, за
# которое черепашка сможет добраться до x2 y2 от текущей позиции
# 
# https://github.com/A-l-E-v/PySynergy/blob/main/U-16/turtle.py
# 

# функция печати координат и перемещения трёх черепах
def t_print():
    print()
    print (f'Черепашка 1 находит в ({t1.x}, {t1.y}) и может пройти {t1.s} за шаг')
    print (f'Черепашка 2 находит в ({t2.x}, {t2.y}) и может пройти {t2.s} за шаг')
    print (f'Черепашка 3 находит в ({t3.x}, {t3.y}) и может пройти {t3.s} за шаг')


# пустой класс ошибки перемещения черепахи на s позиций
class sZero(ValueError):
    pass

class Turtle():

# конструктор координат и перемещения s
    def __init__(self, x = 0, y = 0, s = 1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s +=1
    
    def degrade (self):
       
        self.s -=1

        if self.s > 0:
            return
        else:
            # ставим черепашки минимальную скорость
            self.s = 1
            raise ValueError(sZero) 
 

t1 = Turtle()
t2 = Turtle(10,10,1)
t3 = Turtle (-2,-3,2)

t_print()

print()
print ('Переместим 1-ую черепашку налево вниз, 2-ую направо вверх, 3-ю направо вниз')

t1.go_left()
t1.go_down()

t2.go_right()
t2.go_up()

t3.go_right()
t3.go_down()

t_print()

print()
print ('Ускорим 1-ую черепашку налево вверх, замедлим 2-ую налево вниз, замедлим 3-ю налево вниз')

t1.evolve()
t1.go_left()
t1.go_down()

try:
    t2.degrade()
except ValueError:
    print ('Черепашка 2 уже на минимальной скорости!')
t2.go_right()
t2.go_up()

try:
    t3.degrade()
except ValueError:
    print ('Черепашка 3 уже на минимальной скорости!')
t3.go_right()
t3.go_down()

t_print()