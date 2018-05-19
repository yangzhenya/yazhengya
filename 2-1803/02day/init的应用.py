class Girl():
	def __init__(self,age,height,address):
		self.age = age
		self.height = height 
		self.address = address
		self.games = []

	def study(self):
		print("学习")
	def opencar(self,car):
		print("一定会开车%s"%car)
	def showage(self):
		print("年龄%d"%self.age)
	def addgames(self,game):
		self.games.append(game)
	def showgames(self):
		for i in  self.games:
			print(i)




louxueman = Girl(12,170,"河南")
louxueman.study()
louxueman.opencar('宝马')
louxueman.showage()
louxueman.addgames("王者")
louxueman.showgames()
print(id(louxueman))

xiaoyuan = Girl(16,180,"河北")
xiaoyuan.study()
xiaoyuan.opencar("奇瑞")
xiaoyuan.addgames("魂斗罗")
xiaoyuan.showage()
xiaoyuan.showgames()
print(id(xiaoyuan))
