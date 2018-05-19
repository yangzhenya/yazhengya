class Cat():
	def __init__(self,name,age):
		self.name = name 
		self.age = age



	def sleep(self,bed,name):
		print("%s正在%s睡觉"%(name,bed)
	



tom  = Cat("汤姆",40)
tom.sleep("席梦思",tom.name)
print(id(tom))


bosimao = Cat("波斯猫",21)
bosimao.sleep("地板",bosimao.name)
print(id(bosimao))
