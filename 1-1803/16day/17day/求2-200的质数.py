def zhishu(x,y):
	for i in range(x,y+1):
		flag = 0 #默认质数
		for j in range(2,i):
			if i%j == 0:
				flag = 1
				break
		if flag == 0:
			print(i)



zhishu(2,200)
