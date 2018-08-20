class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)

    def switch(self):
        self.x, self.y = self.y, self.x
        print(self.x, self.y)
        print('transition complete')

p = Point(1,2)
print(p)
q=p.switch()
print(q)
