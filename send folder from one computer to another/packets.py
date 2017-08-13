import socket

#use to string replace from last
def sRFL(stringToBeReplace,currentString):
	if len(currentString)>len(stringToBeReplace):
		print "string can't be replaced "
	else:
		pos = len(stringToBeReplace)-len(currentString)
		return stringToBeReplace[0:pos]+currentString


def reciveFile(writeFile,socket_,address):
	while True:
		recivedPacket,recad=socket_.recvfrom(19020)
		socket_.sendto(recivedPacket[0:20],address)
		ack,recad=socket_.recvfrom(20)
		if ack=="acknoledged":
			if recivedPacket[20:19020]:
				print recivedPacket[0:20]
				writeFile.write(recivedPacket[20:19020])
			if not recivedPacket[20:19020]:
				writeFile.close()
				break
		elif ack=="notacknoledged":
			continue
	return 'fileOver'	

#to send file
def sFile(opnedFile,client,addressServer):
	ackNo=0
	ack='null'
	while True:
		fileData=opnedFile.read(19000)
		ackStr = "xhxhxhxhxhxhxhxhxhxh"
		ackNo +=1
		ack = sRFL(ackStr,`ackNo`)
		packet=ack+fileData
		while True:
			print "packet -" +ack+ "- sent "
			client.sendto(packet,addressServer)
			confirmAck,addr=client.recvfrom(20)
			if confirmAck==ack:
				client.sendto('acknoledged',addressServer)
				break
			elif confirmAck!=ack:
				client.sendto('notacknoledged',addressServer)
				continue
		if not packet[20:1900]:
			opnedFile.close()
			break
	return "fileOver"
