class Pig():
	def sleep(self):
		print("睡")
	def eat(self):
		print("吃")
	def introduce(self):
		print("我叫%s年龄%d颜色%s"%(self.name,self.age,self.color))







peiqi = Pig()
peiqi.sleep()
peiqi.eat()
peiqi.name = "小猪佩琪"
peiqi.age = 12
peiqi.color = "粉色"
peiqi.introduce()

qz = Pig()
qz.sleep()
qz.eat()
qz.name = "小猪乔治"
qz.age = 12
qz.color = "黑色"
qz.introduce()
