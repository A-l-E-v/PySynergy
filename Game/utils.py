from random import randint as rand

# условная генерация
def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

# случайная ячейка игрового поля
def randcell(w,h):
    tw = rand(0, w - 1) 
    th = rand(0, h - 1)
    return (th, tw)


def randcell2(x, y):   
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
     # 0 - вверх, 1 - направо, 2 - вниз, 3 - налево
    t = rand(0,3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)
