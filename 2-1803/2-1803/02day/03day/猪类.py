class Pig():
	def sleep(self):
		print("睡觉觉")
	def eat(self):
		print("猪饲料")
	def introduce(self):
		print("名字是%s年龄是%d颜色是%s"%(self.name,self.age,self.color))




peiqi = Pig()
peiqi.name = "小猪佩奇"
peiqi.age = 12
peiqi.color = "蓝色"
peiqi.sleep()
peiqi.eat()
peiqi.introduce()




qz = Pig()
qz.name = "乔治"
qz.age = 10
qz.color = "黑色"
qz.sleep()
qz.eat()
qz.introduce()
