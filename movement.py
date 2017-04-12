from interfacing import motor_rear, motor_front

linear = 0  # 1 for forward, 0 for stop, -1 for reverse
turn = 0  # -1 for left, 1 for right, 0 for center

speed = 0.3

direction = (linear, turn)


def bot_stop():
    motor_front.forward(0)
    motor_rear.forward(0)


def bot_left():
    motor_front.backward(0.5)


def bot_right():
    motor_front.forward(0.5)


def bot_forward(turn_flag):
    if turn_flag == 0:
        motor_front.forward(0)
    elif turn_flag == 1:
        motor_front.forward(speed)
    else:
        motor_front.backward(speed)
    motor_rear.forward(speed)


def bot_backward(turn_flag):
    if turn_flag == 0:
        motor_front.forward(0)
    elif turn_flag == 1:
        motor_front.forward(speed)
    else:
        motor_front.backward(speed)
    motor_rear.backward(speed)


def bot_map(direction):
    if direction[0] == 1:
        bot_forward(direction[1])
    elif direction[0] == -1:
        bot_backward(direction[1])
    else:
        bot_stop()
