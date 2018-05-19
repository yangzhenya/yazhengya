def cfkz(x,y):
	
	for i in range(x,y):
		for j in range(x,i+1):
			print%d*%d=%d"%(j,i,i*j),end="\t")
		print("")


cfkz(1,10)
