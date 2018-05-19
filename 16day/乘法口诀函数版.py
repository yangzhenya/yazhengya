def cfkz(x,y):
	for i in range(x,y):
		for k in range (x,x+1):
			print("%d*%d=%d"%(i,k,i*k)),end="/t")
		print("")



cfkz(1,10)
