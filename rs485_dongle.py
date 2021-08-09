import serial
from time import sleep
import os



s4= serial.Serial(port="/dev/ttyO4",baudrate=115200,bytesize=8,stopbits=1,timeout=1)
cmd="echo 12345678 > /dev/ttyO4"
os.system(cmd)
sleep(0.2)
s=s4.readline().strip()
print(s)

if s=="12345678":
	exit(0)
exit(1)
