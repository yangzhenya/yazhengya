#列表有序的
#字典无序

cards = [{"name":"李明瑞","age":12},{"name":"伊天","age":12},{"name":"韩迪","age":13}]
while True:
		name = input("请输入名字")
		flag = 0 #假设名字不在列表的字典里面
		#验证我的假设
		for temp in cards:
				if name == temp["name"]:
			        	flag = 1#赋值为1
				        break


		if flag == 1:#找到了
				print("重复了")
				continue
		age = input("请输入年龄")
		#name = "伊天"
		#添加之前 你需要判断列表有没有我输入名字的这个
		#temp = {"name:"李明瑞"，"age":12}#第二次
		#"伊天" = temp["name"] #第二次

		#if flag ==0: #没有找到才可以添加
		dict = {}
		dict["name"] = name
		print("添加成功")
