class Animal():
	def eat(self):
		print("吃")

class Dog(Animal):
	def eat(self):
		print("狗吃骨头")

	def wark(self):
		print("汪汪叫")





class xtq(Dog):
	def wark(self):
		print("嗷嗷叫")
		super().wark()




taidi = Dog()
taidi.eat()
xiaotq = xtq()
xiaotq.wark()
