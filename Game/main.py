from map import Map
from helicopter import Helicopter as helico
from clouds import Clouds
import time
import os
from pynput import keyboard
import json

TIME_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 10, 10
CLOUDS_UPDATE = 150

# слой облаков
clouds = Clouds(MAP_W, MAP_H)

# вертолёт
helico = helico(MAP_W, MAP_H)

# карта игры
game_map = Map(MAP_W, MAP_H)

# генерация элементов игры
game_map.generate_forest(3, 10)
game_map.generate_rivers(25)
game_map.generate_upgrade_shop()
game_map.generate_hospital()

# матрица смещения вертолёта
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

# обработка клавиш
def process_key(key):
    global game_map, clouds, helico, tick
    c = key.char.lower()

    # перемещение вертолёта
    if c in MOVES.keys():
        helico.move(MOVES[c][0], MOVES[c][1])
    
    # сохранение игры в файл
    if c == 'n':
        data = {'helicopter': helico.export_data(),
                'map' : game_map.export_data(),
                'clouds' : clouds.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    
    # восстановление игры из файла
    if c == 'm':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick']
            game_map.import_data(data['map'])
            clouds.import_data(data['clouds'])
            helico.import_data(data['helicopter'])
    else:
        None

# обработчик клавиатуры
listener = keyboard.Listener(on_release=process_key)
listener.start()


tick = 1

# бесконечный цикл игры
while True:
    os.system('clear')
    print('TICK= ', tick)
    game_map.process_helicopter(helico, clouds)
    helico.print_stats()
    game_map.print_map(helico, clouds)
    tick += 1
    time.sleep(TIME_SLEEP)

    # обновление игровых элементов
    if tick % TREE_UPDATE == 0:
        game_map.generate_tree()
    if tick % FIRE_UPDATE == 0:
        game_map.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()