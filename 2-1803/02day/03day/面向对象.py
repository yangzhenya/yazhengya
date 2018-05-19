class Car():
	def __init__(self):
		self.color = "黄色"
	def __str__(self):
		return "车的颜色是%s"%self.color
	def move(self):
		print("车在跑")
	def stop(self):
		print("车停了")





bmw = Car()
bmw.move()
print("颜色是%s"%bmw.color)
bmw.stop()
print(bmw)

bc = Car()
bc.move()
bc.stop()
print(bc)
