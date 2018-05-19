class Person(object):
	def __init__(self,name,age,taste):
		self.name = name 
		self.age = age 
		self.taste = taste
	def showPerson(self):
		print(self.name)
		print(self._age)
		print(self.__taste)
	def dowork(self):
		self._work()
		self.__away()
	def _work(self):
		print("m")
