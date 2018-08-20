class A(object):
    def __eq__(self, other):
        print ("A __eq__ called")
        return self.value == other
class B(object):
    def __eq__(self, other):
        print ("B __eq__ called")
        return self.value == other

a=A()
a.value=3
b=B()
b.value=5
print('2:before')
a==b
print('2:after')

