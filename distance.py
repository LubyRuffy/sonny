from gpiozero import DistanceSensor
from interfacing import echo,trigger
from time import sleep

sensor = DistanceSensor(echo, trigger)

def calculate_distance():
    return round(sensor.distance*100,2)
    sleep(0.2)