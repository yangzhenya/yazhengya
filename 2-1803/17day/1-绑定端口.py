from socket import *
s = socket(AF_INET,SOCk_DGRAM)
s.bind(('',4547))

s.sendto("哈哈".encode("gb2312"),("192.168.1,111",8080))

while True:
	content,info = s.recvfrom(1024)
	print("%s---%s"%(content.decode("gb2312"),info[0]))

soclose()
