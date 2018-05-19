class Dog(object):
	_instance = None
	def __new__(cls):
		if cls_instance == None:
			cls._instance = object.__new__(cls)
			return cls._instance
		else:
			return cls._instance
	def __init__(self,name):
		self.name = name 

dog1 = Dog("xiaoming")
dog2 = Dog("xiaohong")
