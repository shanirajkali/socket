import socket
import packets
import os
socket_=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
portServer=8778
portClient=8779
socket_.bind((host,portServer))
addressClient=(host,portClient)
os.makedirs('recivedDir')
files,addr=socket_.recvfrom(100)
i=int(files)
j=0
currdir=os.getcwd()
os.chdir('./'+'recivedDir')
while j<i:
	while True:
		dirName,addr=socket_.recvfrom(100)
		f=open(dirName,'wb')
		packets.reciveFile(f,socket_,addressClient)	

		#if exit=="exit":
		break
	j+=1	
socket_.close()
