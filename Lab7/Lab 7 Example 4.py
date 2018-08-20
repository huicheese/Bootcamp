import math

class Point(object):
	def __init__(self,x,y): # Constructor
		self.x = x
		self.y = y
	def magnitude(self): # magnitude (get) method
		return math.sqrt(self.x**2 + self.y**2)

a=Point(3,4)
print(a)
print(a.x)
b=a.magnitude()
print(b)

