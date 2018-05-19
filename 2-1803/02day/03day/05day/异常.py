try:
	print(num)
	print("哈哈哈哈哈哈哈")
except (NameError,FileNotFoundError):
	print("出错了")
except Exception as ret:
	print("大错特错")
	print(ret)

else:
	print("没有错误会走这")

finally:
	print("有错没错都走")

print("呵呵呵呵呵呵呵呵呵")
