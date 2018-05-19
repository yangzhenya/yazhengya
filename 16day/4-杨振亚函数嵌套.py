#import time
def up_class():
	print("杨振亚正在上课")
	call_phone()
	print("杨振亚继续上课")
def call_phone():
	for i in range(10):
		print("杨振亚接电话")
		time.sleep(1)


up_class()
