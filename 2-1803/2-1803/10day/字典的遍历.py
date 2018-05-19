list = [{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in list:
#	print(i)
	for k,v in i.items():
	#	print(k,v)
		for a,b in v.items():
			print(k,a,b)
