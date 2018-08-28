#def register():

def getrecords():
    file = open("C:/Users/Huicheese/Documents/MSSD/Bootcamp/MSSD-Bootcamp-Labs/Lab 9/UsernameNPassword.txt", "r")
    for line in file:
        data = dict(x.split(',') for x in file.split('\n'))
    return data.get()

getrecords()

#def check(username, password):

#def successcheck():
