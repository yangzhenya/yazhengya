class Home():
	def __init__(self,area,name,price,address):
		self.area = area
		self.name = name
		self.price = price
		self.address = address
	def __str__(self):
		msg = ("房子的名字%s房子的面积%d房子的价格%d房子的地址%s"%(self.name,self.area,self.price,self.address))
		return msg
class Bed():
	def __init__(self,area,name):
		self.area = area
		self.name = name
	def __str__(self):
		msg = ("床的面积是%d床的名字是%s"%(self.area,self.name))
		return msg

myhome = Home(120,"塞上雅居",1200,"普吉岛")
print(myhome)

newbed = Bed(4,"席梦思")
print(newbed)




