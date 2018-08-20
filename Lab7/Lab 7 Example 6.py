import math


class Point(object):
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def magnitude(self):  # magnitude (get) method
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def drive(self, distance):
        """ drive the car a given distance if it has 	enough fuel """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            self.odometer += distance
        return distance

    def translate_abc(self, dx, dy):  # translate (set) method
        self.x = x + dx
        self.y = y + dy
        return self.x, self.y


a = Point(3, 4)
d = Point(5, 6)
print(a)
print(a.x)
b = a.magnitude()
print(b)
a.fuel=400
a.odometer=10000
d=a.drive(300)
print('d is :',d, ':\n')
print('a.odometer is ', a.odometer)
x=1
y=2
e=a.translate_abc(1,2)
print(e)


