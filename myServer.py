from socket import socket, AF_INET, SOCK_DGRAM
import sys

myPort = int(sys.argv[1])  		#set to the port received by arguments
myIP = "0.0.0.0"
parentPort = int(sys.argv[3]) 	#set to the port received by arguments
parentIP = sys.argv[2] 			#set to the ip received by arguments
ipsFileName = sys.argv[4]		#set to the name received by arguments

sServer = socket(AF_INET,SOCK_DGRAM)	#create a udp socket above IP.
sClient = socket(AF_INET,SOCK_DGRAM)	#create a udp socket above IP.
sClient.bind((myIP,myPort))				#bind the client socket to self ip.

maps ={}	#creates dictionary for url ip pairs.
with open(ipsFileName) as openfileobject:	#open document
    for line in openfileobject:				#for every line in document
	if len(line.split(','))==2:				#if there are two parts seperated by ,
	        maps[line.split(',')[0]]=(line.split(',')[1]).split('\r')[0] 
			#insert to dictionary maps the first part and set its value to the second one.

while True:		#now loop 
    url_request,sender_info = sClient.recvfrom(2048)	#wait and listen to client socket
    if url_request in maps:	#if received something that is in maps dictionary then:
        sClient.sendto(maps[url_request],sender_info)	#send back the value of it.
    elif parentIP != "-1":	#if not in map and parent server exists
        sServer.sendto(url_request,(parentIP,parentPort))	#send parent server the request
        ip_request,server_info = sServer.recvfrom(2048)		#receive from parent the answer
        maps[url_request]=ip_request						#add the answer to current maps
        with open(ipsFileName,"a") as mapsFile:				#open file to add a list
            mapsFile.write((url_request+','+ip_request+'\r'))#add the line to the file.
        sClient.sendto(ip_request,sender_info)				#send the client the answer.
    elif  parentIP == "-1":	#if is parent and no answer then return sorry - just for usefulness.
        sClient.sendto("sorry",sender_info)	
                                   
        
