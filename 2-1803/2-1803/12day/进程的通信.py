from multiprocessing import Manager,Pool
import os, time,random
def reader(q):
	print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid())
