class Person():
	def sleep(self):
		print("睡觉")
	def eat(self):
		print("吃吃")
	def study(self):
		print("学习")
	def introduce(self):
		print("我的名字叫%s身高%d体重%d"%(self.name,self.height,self.weight))






yangzhenya = Person()
yangzhenya.sleep()
yangzhenya.eat()
yangzhenya.study()
yangzhenya.name = "杨振亚"
yangzhenya.height = 180
yangzhenya.weight = 80
yangzhenya.introduce()



wanglin = Person()
wanglin.sleep()
wanglin.eat()
wanglin.study()
wanglin.name = "王淋"
wanglin.height = 170
wanglin.weight = 65
wanglin.introduce()
