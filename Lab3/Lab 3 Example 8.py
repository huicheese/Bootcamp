def is_prime(number):
    divisor = 2
    if number == 1:
        return True
    elif number > 1:
        while divisor < number:
            if number % divisor == 0:
                return False
            divisor += 1
        return True
    else:
        return None
a=is_prime(4)
print(a)
