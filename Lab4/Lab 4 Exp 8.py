x, y = (1, 2) # (1, 2) is a tuple
print(x, type(x)) # 1, <class 'int'>

def get_low_high(values):
   return min(values), max(values)

my_list = (1, 5, 7, 8)
low, high = get_low_high(my_list)
print(low, type(low)) # -12, <class 'int'>

z = get_low_high(my_list)
print(z, type(z)) # (-12, 45), <class 'tuple'>
