import serial
import time
port = serial.Serial("/dev/rfcomm0", baudrate=9600)
 
# reading and writing data from and to arduino serially.                                      
# rfcomm0 -> this could be different
while True:
	print "DIGITAL LOGIC -- > SENDING..."
	port.write(str(3))
	#string from hub "B33R 1 1000" 
	#
	rcv = port.readline()
	count = int(recv[7:])
	if rcv:
	   print(rcv)
	time.sleep( 3 )