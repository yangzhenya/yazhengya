list = [1,23,54,12,78,96,52,21,4,56,41]



for i in range (len(list)):
	for k in range(i+1,len(list)):
		if list[i] > list[k]:
			list[i],list[k] = list[k],list[i]
print(list)


key = 52
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center = center - 1
		elif list[center] < key:
			center = center + 1
		elif list[center] == key:
				print("要找的数字是%d在索引%d"%(key,center))
				break
		else: 
				print("查无结果")
