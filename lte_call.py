import serial
from time import sleep
import os



s4= serial.Serial(port="/dev/ttyUSB2",baudrate=115200,bytesize=8,stopbits=1,timeout=1)
while True:
	s4.write("ATD13556722917;")
	sleep(3)
	s=s4.readline().strip()
	print(s)
	s4.write("ATH")
	sleep(2)

if s=="12345678":
	exit(0)
exit(1)
