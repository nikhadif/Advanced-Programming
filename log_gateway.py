from time import sleep
import serial
import datetime
encoding = 'utf-8'
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600)

data = 	{
		"x":
			{"distance":0.0,"rssi":0.0},
		"y":
			{"distance":0.0 ,"rssi":0.0},	
		"z":
			{"distance":0.0,"rssi":0.0}
		}

coordinate = ("x","y","z")
while True:

	ser_decode =ser.readline().decode("utf-8", "ignore")

	ser_decode = ser_decode.replace("\r","")
	ser_decode = ser_decode.replace("\n","")

	ser_decode = ser_decode.split(",")
	print (ser_decode)
	
	if ser_decode[0]  == '0':
		if int(ser_decode[1]) >1500:
			continue
		else:			# x -axis
			data["x"]["distance"] = float(ser_decode[1])
			data["x"]["rssi"] = float(ser_decode[2])
	elif ser_decode[0]  == '1':			# x -axis
		if int(ser_decode[1]) >1500:
			continue
		else:
			data["y"]["distance"] = float(ser_decode[1])
			data["y"]["rssi"] = float(ser_decode[2])
	elif ser_decode[0]  == '2':			# x -axis
		if int(ser_decode[1]) >1500:
			continue
		else:
			data["z"]["distance"] = float(ser_decode[1])
			data["z"]["rssi"] = float(ser_decode[2])
	else:
		continue
	print (data)
	
	for choice in coordinate:
		if ser_decode[0] == choice:
			last_digit_index = ser_decode.index("'")
			distance = float(ser_decode[2:last_digit_index])
			if distance < 1500 :
				
				data[choice]["distance"] = distance
			
				char_i_index = ser_decode.index("I")
				char_r_index = ser_decode.index("\r")
				signal_strength = float(ser_decode[char_i_index+2:char_r_index])
				data[choice]["rssi"] = signal_strength
	with open("time.txt",'a') as out:
		out.write(str(data))
		out.write("\n")

	print (ser.readline())
	sleep(.1)
#since 3.30pm

