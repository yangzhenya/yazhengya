class Person():
	def __init__ (self,money):
		self._money = money



	def getmoney(self):
		return self._money



	def setmoney(self,money):
		self._money = money
		if money <= 0:
			print("输入有误")
		else:
			print("输入正确")






xiaoming = Person()
xiaoming.setmoney(20)	
