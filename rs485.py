import serial
from time import sleep



s1= serial.Serial(port="/dev/ttyO1",baudrate=115200,bytesize=8,stopbits=1,timeout=1)
s4= serial.Serial(port="/dev/ttyO4",baudrate=115200,bytesize=8,stopbits=1,timeout=1)

s1.write("helloworld\r\n");
sleep(0.2)
s=s4.readline().strip()
print(s)

if s=="helloworld":
	exit(0)
exit(1)
