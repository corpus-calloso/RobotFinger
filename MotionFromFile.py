######################################################################
# New file for file reading robot control
######################################################################
import time

#Variables:
#servoPin - is the pin the servo is connected to, restPosition - The position the finger goes to before and after finnisheing the task, comPort - is the port the Ardruino is connected to
servoPin = 3
restPosition = 90
comPort = "COM5"

# create the servo & arduino services
arduino = Runtime.start("arduino","Arduino")
servo = Runtime.start("servo","Servo")

#connect ardruino and attache servo
arduino.connect(comPort)
servo.attach(arduino.getName(), servoPin)

# TODO - set limits
servo.setMinMax(0, 180)
servo.map(0, 180, 0, 180)
servo.setVelocity(-1)

#data array
txt = open("Moves.txt", "r")
moves = txt.read().split(",")
#moves = [20,90,160]
txt.close()

# move servo
servo.moveTo(restPosition)

for x in moves:
	print(x)
	servo.moveTo(x) #Here the MRL for some reason gives error ... please check and give feedback
	time.sleep(1)
