class Dog():
	def __init__(self,name):
		self.name = name 
	def wark(self):
		print("旺旺叫")

	@classmethod
	def test(cls):
		print("这是类方法")




taidi = Dog("泰迪")
print("taidi.name")
taidi.wark()
Dog.test()
taidi.test()
