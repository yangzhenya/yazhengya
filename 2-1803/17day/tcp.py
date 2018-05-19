from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind('',6688)
s.listen(6)

newSocket,info = s.accept()

while True:
	msg = newSocket.recv(1024)
	if len(msg) == 0:
		break
	print(msg.decode('gb2312'))
newSocket.close()

s.close()
