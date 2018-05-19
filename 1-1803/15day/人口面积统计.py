list = [{"北京":{"面积":"1000平","人口":"2000万"},"上海":{"面积":"2000平","人口":"3000w"}}]
for i in list:
#	print(i)
	for k,v in i.items():
#		print(k,v)
		for a,b in v.items():
			print(k,a,b)
