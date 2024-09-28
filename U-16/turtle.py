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

    def go_up():
        self.y +=s

    def go_down():
        self.y -=s

    def go_left():
        self.x -=s
    
    def go_right():
        self.x +=s
    
    def evolve():
        self.s +=1
    
    def degrade ():
       
        self.s -=1

        if s > 0:
            return
        else:
            raise ValueError(sZero) 
 

t1 = Turtle()
t2 = Turtle(10,10,1)
t3 = Turtle (-2,-3,2)

t_print()