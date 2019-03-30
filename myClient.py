from socket import socket, AF_INET, SOCK_DGRAM
import sys

serverIP = sys.argv[1] 			#set server ip from arguments.
serverPort = int(sys.argv[2])	#set server port from arguments.

sSend = socket(AF_INET, SOCK_DGRAM)	#create udp socket above IP.

msg = raw_input("")			#get input

while not msg == 'quit':
	sSend.sendto(msg,(serverIP,serverPort))		#send request to server.
	data, sender_info = sSend.recvfrom(2048)	#receive answer from server.
	print data									#print the answer.
	msg = raw_input("")							#get input
sSend.close()
