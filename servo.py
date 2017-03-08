from interfacing import servo

def sweep():
	for theta in range(-90,95,5):
		servo.angle = theta