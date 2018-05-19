class Pig():
	def eat(self):
		print("猪饲料")
	def sleep(self):
		print("哼哼哼")
	def introduce(self):
		print("我叫%s年龄%d颜色%s"%(self.name,self.age,self.color))






peiqi = Pig()
peiqi.eat()
peiqi.sleep()
peiqi.name = "小猪佩琪"
peiqi.age = 15
peiqi.color = "粉色"
peiqi.introduce()




qz = Pig()
qz.eat()
qz.sleep()
qz.name = "小猪乔治"
qz.age = 10
qz.color = "蓝色"
qz.introduce()
