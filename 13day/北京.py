list = [{"beijing":{"mianji":1290,"renkou":12313},"shanghai":{"mianji":12331,"renkou":12313}}]
for i in list:
	#print(i)
	for k,v in i.itmes():
		#print(k,v)
		for a,b in v,itmes():
			print(k,a,b)



