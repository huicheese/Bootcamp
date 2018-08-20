from math import pi as pi

def area_vol_cylinder(radius, length):
    area = radius**2*pi
    volume = area*length
    return area, volume
a,b=area_vol_cylinder(5,5)
print(a)
print(b)
for i in [1,2,3]:
print(i)