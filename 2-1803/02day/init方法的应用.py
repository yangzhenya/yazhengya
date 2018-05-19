class Car():
	def __init__(self,name,price,color):
		self.name = name
		self.price = price
		self.color = color
	def move(self):
		print("车在跑")




bmw = Car("宝马",200,"黑色")
bmw.move()
