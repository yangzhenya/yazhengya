class Person():
	def __init__(self):
		self.money = 100

	def getMoney(self):
		return self.__money
	def setMoney(self,money):
		if money <= 0:
			print("传入金额有误")
		else:
			self.__money = money



xiaoming = Person()
xiaoming.__money = -100
xiaoming.setMoney(20)
print(xiaoming.getMoney())
xiaoming.__money
