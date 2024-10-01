from utils import randcell
import os


# класс Вертолёт
class Helicopter:

    # инициализация класса
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.h = h
        self.w = w
        self.tank = 0    
        self.mxtank = 1
        self.score = 0
        self.lives = 20
        if (rx >= 0 or ry >= 0 or rx < self.h or ry < self.w):
            self.x = rx
            self.y = ry

    # обработка смещения
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    # вывод статистики игры
    def print_stats(self):
        print("🥡 ", self.tank, '/', self.mxtank, sep="", end=" | ")
        print("🏆 ", self.score, end=" | ")
        print("💛 ", self.lives)

    # конец игры и вывод очков
    def game_over(self):
        os.system("cls")
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('                             ')
        print("GAME OVER, YOUR SCORE IS", self.score)
        print('                             ')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        exit(0)

    # экспорт данных
    def export_data(self):
        return {"score": self.score,
                "lives": self.lives,
                "x": self.x, "y": self.y,
                "tank": self.tank, "mxtank": self.mxtank}

    # импорт данных
    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 3
        self.score = data["score"] or 0