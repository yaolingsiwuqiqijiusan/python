import socket
import struct

while 1:
	int_ip = input("Please input your ip:\n")
	ip=socket.inet_ntoa(struct.pack('I',socket.htonl(int_ip)))
	print("ip,", ip)
