list = [2,5,85,65,54,45,32,12,1,58,74,5,65,6]
for i in range(len(list)):
	for k in range(i+1,len(list)):
		if list[i] > list[k]:
			list[i],list[k] = list[k],list[i]
print(list)

key = 58
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center = center-1
		elif list[center] < key:
			center = center+1
		elif list[center] == key:
			print("要找的数字是%d在索引%d"%(center,key))
			break
		else:
			print("查无此数字")
			
