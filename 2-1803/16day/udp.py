from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto("哈哈哈哈哈哈哈哈哈哈哈哈哈".encode("gb2312"),("192.168.19.122",8080))



s.close()
