list = [9,24,1,25,45,21,23,42,58,56,46,14]
for i in range(len(list)):	 #循环范围0~12
	for k in range (i+1,len(list)):
		if list[i] > list[k]: #比较前面和后面的两个数字
			list[i],list[k] = list[k],list[i]  #前面大于后面就互换

print(list)

