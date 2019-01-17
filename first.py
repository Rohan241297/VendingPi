import RPi.GPIO as gp

gp.setmode(gp.BOARD)
gp.setup(3,gp.IN)

while True:
	if gp.input(3) == 1:
		print("High")
	else:
		print("LOW")
