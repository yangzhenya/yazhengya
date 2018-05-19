#注册
def register (phone,pwd):
	result = isphone(phone)
	if result:
		print("注册成功")
	else:
		print("注册失败")

#登录
def	ligin(phone,pwd):
	result = isphone(phone)
	if result:
		print("登录成功")
	else:
		print("登录失败")

def isphone(phone):

