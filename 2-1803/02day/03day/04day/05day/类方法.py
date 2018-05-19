class Dog():
	def __init__(self,name):
		self.name = name 



	@classmethod
	def getCountry(cls):
		return cls.Country






taidi = Dog()
taidi.name = "泰迪"
print(taidi.getCountry()):
