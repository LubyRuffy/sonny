from random import random, seed
from json import loads, dumps
from movement import bot_map, direction


crash_flag = 0
seed()
values = {'count': 0, 'weight': random(),
              'threshold': 0, 'flag': 0, 'alpha': 50}

def init():  # first time write to file
    global values
    dump = open('dump.txt', 'w')
    values = dumps(values)
    dump.write(values)
    dump.close()


def learn(distance):
    global direction, values
    dump = open('dump.txt', 'r')
    #  read file
    values = dump.read()
    dump.close()
    values = loads(values)
    print values
    weight = values['weight']
    print weight
    threshold = values['threshold']
    print threshold
    product = distance * weight
    if product < threshold:
        direction = (0, 0)
        bot_map(direction)
        "ruka"
