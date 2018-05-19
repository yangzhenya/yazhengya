def makeBold(fn):
	def wrapped():
		return "哈哈哈"
	return wrapped

def makeItalic(fn):
	def wrapped():
		return "呵呵呵"
	return wrapped

@makeBold
def test1():
	return "hello world-1"
@makeItalic
def test2():
	return "hello world-2"

@makeBold
@makeItalic
def test3():
	return "hello world-3"

print(test1())
print(test2())
print(test3())
