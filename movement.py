from interfacing import motor_rear, motor_front

linear = 0  # 1 for forward, 0 for stop, -1 for reverse
turn = 0  # -1 for left, 1 for right, 0 for center

speed = 0.3

direction = (linear, turn)


def bot_stop():
    motor_front.forward(0)
    motor_rear.forward(0)


def bot_forward(turn_flag):
    if turn_flag == 0:
        motor_front.forward(0)
    elif turn_flag == 1:
        motor_front.forward(1)
    else:
        motor_front.backward(1)
    motor_rear.forward(speed)


def bot_backward(turn_flag):
    if turn_flag == 0:
        motor_front.forward(0)
    elif turn_flag == 1:
        motor_front.forward(1)
    else:
        motor_front.backward(1)
    motor_rear.backward(speed)


def bot_map(direction):
    if direction[linear] == 1:
        bot_forward(direction[turn])
    elif direction[linear] == -1:
        bot_backward(direction[turn])
    else:
        bot_stop()
