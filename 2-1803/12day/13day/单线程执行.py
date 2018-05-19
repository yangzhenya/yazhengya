import threading
import time
 
def saySorry():
	print("唱歌")
	time.sleep(2)

if _name_ == "_main_":
	for i in range(5):
		saySorry()
