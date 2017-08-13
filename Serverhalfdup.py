import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         
host = socket.gethostname()
port = 6791        
s.bind((host, port))
print "listening..."      
while True:
      filename,addr=s.recvfrom(1024)
      print "Filename recieving.."
      s.sendto("1",addr)
      f=open("recieving"+filename,"wb")
      filec,addr=s.recvfrom(1024)
      c=1
      print len(filec)
      while len(filec)==1024:
        f.write(filec)
        s.sendto("yes",(addr[0],int(addr[1])))
        filec,addr=s.recvfrom(1024)
        c+=1
        #print len(fc)
      f.write(filec)
      s.sendto("yes",(addr[0],int(addr[1])))
      print c
      print "file recieved"

      fname=raw_input("Enter filename:>>")
      if fname=='q':
           break
      f=open(fname,"rb")
      s.sendto(fname,addr)
      data,add=s.recvfrom(2048)
      if add==addr:
          print "Filename recieved"
      e=1
      while e==1:
          print "Sending file..."
          local=f.read(2048)
          c=0
          while local:
              c+=1
              s.sendto(local,addr)
              datam,a=s.recvfrom(2048)
              local=f.read(2048)
          print c
          print "file Sent"
          e=0
s.close()
f.close()