list = [2,8,13,32,35,40,45,50,53,65,85]
key = 45
center = int(len(list)/2)#这里一定要加int，防止列表是偶数时出现浮点数据
if key in list:
		while True: #建立一个死循环，直到找到key
				if list[center] > key: #key在数组左边
						center = center-1
				elif list[center] < key: #key在数组右边
						center = center+1
				elif list[center] == key: #key在数组中间
					print("要查找的数字是%d在索引%d"%(key,center))
					break
				else:
					print("没有此数字")

