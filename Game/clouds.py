from utils import randbool


# класс слоя облаков
class Clouds:

    # инициализация класса
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    # обновление слоя
    def update(self, r=1, mxr=10, g=1, mxg=10):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    # подготовка данных на экспорт
    def export_data(self):
        return{"cells": self.cells}
    
    # загрузка данных
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]