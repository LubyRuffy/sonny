from time import sleep
from interfacing import sensor


def calculate_distance():
    return round(sensor.distance*100,2)
    sleep(0.2)