from socket import *
from threading import Thread
s = None
ip = ''
port = 0
def send():
	global s
	global ip
	global port
	content = input("\r请输入内容")
	s.senfto(content.encode("gb2312"),ip,port)
def recv():
	while True:
		msg = s.recvfrom(1024)
		print("%s---%s"%(msg[0].decode('gb2312'),msg[1][0]))
def main():
	global s
	global ip
	global port
	ip = input("请输入对方ip")
	port = int(input("请输入对方端口:"))
	s = scoket(AF_INET,SOCK_RGRAM)

	#绑定端口
	s.bind ('', 7888)
	
	t = thread(target=send)
	t1 = Thread(target=recv)
	t.start()
	t1.start()
	t.join()
	t1.join()

if __name__ --"__main__":


