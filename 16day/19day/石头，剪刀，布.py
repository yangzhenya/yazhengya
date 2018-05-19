import random
i = 0
while i < 10:
	playerStr = input("请输入[0剪刀 1石头 2布]")
	player = int(playerStr)
	computer = random.randint(0, 2)
	if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
		print("你赢了")
	elif player == computer:
		print("平局")
	else:
		print("电脑赢了")
	i += 1
