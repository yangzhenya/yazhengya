class Person():
	def sleep(self):
		print("睡觉")
	def eat(self):
		print("吃饭")
	def study(self):
		print("学习")
	def introduce(self):
		print("我的名字叫%s体重%d身高%d"%(self.name,self.weight,self.height))







yangzhenya = Person()
yangzhenya.sleep()
yangzhenya.eat()
yangzhenya.study()
yangzhenya.name = "杨振亚"
yangzhenya.weight = 80
yangzhenya.height = 180
yangzhenya.introduce()

