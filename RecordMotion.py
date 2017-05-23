##################################################################
# Record motion new
##################################################################

#create file for loging the data
txt = open("Log.txt", "w")
txt.write("90,")
txt.close
txt = open("Log.txt", "a")


# create the leap motion service
leap = Runtime.createAndStart("leap","LeapMotion")
# connect python as a listener for the onLeapData callback
leap.addLeapDataListener(python)
# start the leap motion watching for valid frames.
leap.startTracking()


# when leap motion data is detected, it will be passed in here
def onLeapData(data):
	if (data.rightHand):
		# if the data has a right hand, print out some info about it.
		data = data.rightHand.index
		data = "" if data == 0 else str(data)+","
		print("Right Index =" + data)
		txt.write(data)

txt.close