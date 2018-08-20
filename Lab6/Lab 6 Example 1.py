def binary_to_decimal(binstr):
    num = 0
    for i,char in enumerate(binstr):
        if char == "1":
            num += 2**(len(binstr)-1 - i)
        elif char != "0":
            print("Invalid binary string!")
            return
    return num

a=binary_to_decimal('100')
print(enumerate('100'))
c=enumerate('100')
print(a)