class showError(Exception):
	def __init__(self,length,atleast):
		super.()__init__()
		self.length = length
		self.atleast = atleast

def main():
	try:
		s = input("请输入")
		if len(s)<3:
			raise ShowError(len(3),3)

	except ShowError as result:
			print(:w)

