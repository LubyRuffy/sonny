from interfacing import front_motor,rear_motor

def forward():
	front_motor.stop()
	rear_motor.forward()

def left():
	front_motor.forward()
	rear_motor.forward()

def right():
	front_motor.backward()
	rear_motor.forward()

def stop():
	front_motor.stop()
	rear_motor.stop()

def backward():
	front_motor.stop()
	rear_motor.backward()