import time 
def up_class():
		print("杨振亚正在听课")
		call_phone()
		print("杨振亚有事出去")


def call_phone():
		for i in range(10):
				print("杨振亚接电话")
				time.sleep(1)

up_class()

