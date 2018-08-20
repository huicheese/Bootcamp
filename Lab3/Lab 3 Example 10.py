def gcd_loop(a,b):
    if a<0 or b<0:
        return None
    if b==0:
        return a
    while not a%b==0:
        a,b = b, a%b
    return b

a=gcd_loop(5,101)
print(a)