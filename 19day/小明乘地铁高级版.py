list = []
all_count = 0#坐的次数
def my_input():
	dict = {} #月份和钱
	sum = 0#记录每月花多少钱
	global all_count #声明要修改变量
	month = int(input("请输入月份"))
	if month <= 0 or month > 12:
			print("输人有误")
			return
	count = int(input("请输入每天坐地铁的次数"))
	if count <= 0:
			print("次数输入有误")
			return
	all_count+=3*count:w
