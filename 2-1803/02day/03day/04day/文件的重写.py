class Animal():
	def eat(self):
		print("吃吃")
	def sleep(self):
		print("睡觉")


class Dog(Animal):
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
xiaotq.sleep()
