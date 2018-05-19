account = "123456"
pwd = "123456"
money = "99999"




l_acc = input("请输入账户")
l_pwad = input("请输入密码")


if l_acc == account and l_pwd == pwd:
	l_money = float(input("请输入取款金额"))
	if money >= l_money:
		print("取了%.02f元,剩余%.02f"%(l_money, money - l_money))
	else:
		print("账户余额不足")
else:
		print("账户不存在")
