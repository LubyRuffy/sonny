from random import random, seed
from ast import literal_eval
from movement import bot_map, direction
from interfacing import reroute_flag

crash_flag = 0

seed()
values = {'count': 0, 'weight': random(),
          'threshold': 0, 'flag': 0, 'alpha': 50}


def init():  # first time write to file
    global values
    dump = open('dump.txt', 'w')
    dump.write(str(values))
    dump.close()


def learn(distance):
    global direction, values, reroute_flag
    dump = open('dump.txt', 'r')
    #  read file
    values = literal_eval(dump.read())
    dump.close()
    weight = values['weight']
    threshold = values['threshold']
    product = distance * weight
    if product < threshold:
        reroute_flag = 1
        print "YAY"
        direction = (0, 0)
        bot_map(direction)
