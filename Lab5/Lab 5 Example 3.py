import random

craps=set([2,3,12])
naturals=set([7,11])

def roll_two_dices():
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    return n1,n2

def print_lose():
    print "You lose"

def print_win():
    print "You win"

def print_point(p):
    print 'point is ',p

def is_craps(n):
        return n in craps

def is_naturals(n):
        return n in naturals

def play_craps():
    point=-1
    while True:
        n1,n2=roll_two_dices()
        sumn=n1+n2
        print 'You rolled %d + %d = %d'%(n1,n2,sumn)
        if point==-1:
            if is_craps(sumn):
                print_lose()
                return 0
            elif is_naturals(sumn):
                print_win()
                return 1
            point=sumn
            print_point(point)
        else:
            if sumn==7:
                print_lose()
                return 0
            elif sumn==point:
                print_win()
                return 1

a=play_craps()
print(a)
