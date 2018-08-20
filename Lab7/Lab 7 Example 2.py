class Point(object):
	def __init__(self,initX,initY): # double underscore
		self.x = initX
		self.y = initY
		print(self.x, self.y)

p = Point(7,6)
print(p)
