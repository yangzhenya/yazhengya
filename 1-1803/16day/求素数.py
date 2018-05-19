def zhishu(x,y):
	for i in range (x,y+1):
		flag = 0 #默认质数
		for k in range(2,i):
			if i%k == 0:
				flag =1
				break
		if flag == 0:
			print(i)

zhishu(2,200)
