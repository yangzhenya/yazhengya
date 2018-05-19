t = ("laowang","laoli","laosong","laozhao")
s = input("请输入一个名字")

if s in list(t):
	print("laogang")
else:
	print("buzai")
if s not in t:
	print("buzai")
else:
	print("zai")

