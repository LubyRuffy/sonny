from random import random, seed
from json import loads, dumps
from movement import bot_map, direction


crash_flag = 0
seed()
turn_radius = 1.5
values = {'count': 0, 'weight': random(),
              'threshold': 0, 'flag': 0, 'alpha': 0.05}

def init():  # first time write to file
    global values
    dump = open('dump.txt', 'w')
    values = dumps(values)
    dump.write(values)
    dump.close()


def learn(distance):
    global direction
    dump = open('dump.txt', 'r')
    #  read file
    values = dump.read()
    dump.close()
    values = loads(values)
    product = distance * values['weight']
    if product < values['threshold']:
        direction = (0, 0)
        bot_map(direction)
