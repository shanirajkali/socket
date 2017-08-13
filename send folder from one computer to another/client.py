import socket
import packets
import os
socket_=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host=socket.gethostname()

portServer=8778
portClient=8779

socket_.bind((host,portClient))
addressServer=(host,portServer)
print addressServer
dirName=raw_input("enter 'file name' : ")
dirList=os.listdir(dirName)
files=len(dirList)
socket_.sendto(`files`,addressServer)
i=0
while i<files: 
	while True:
		socket_.sendto(dirList[i],addressServer)
		f=open(dirList[i],'rb')
		packets.sFile(f,socket_,addressServer)
		
		#if exit=="exit":	
		break
	i+=1	
socket_.close()
