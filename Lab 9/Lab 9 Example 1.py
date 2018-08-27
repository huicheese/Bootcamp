mode = input("Encrypt/Decrypt?")
msg = input("What is the message that you would like to input? ")
key = input("Key? ")

class Caeser(object):
    def __init__(self, mode, msg, key):
        self._mode = mode
        self._msg = msg
        self._key = key

    def checkMode(self):
        if self._mode not in 'encrypt e Encrypt E decrypt d Decrypt D'.split():
            print("Enter either encrypt or decrypt: ")
            self.checkMode(self)
        else:
            maxkey = 26
            try:
                key = int(self._key)
                if int(key) >= 1 and int(key) <= maxkey:
                    self.CEncrypt(self._mode, self._msg, self._key)
                else:
                    print("Error in key size ")
                    self.checkMode(self)
            except ValueError:
                print("Please enter valid key: ")
                self.checkMode(self)

    def CEncrypt(self, mode, msg, key):
        self._key = int(key)

        if mode[0] == "d":
            self._key = -key

        encrypted = ''
        for i in msg:
            if i.isalpha():
                num = ord(i)
                num += self._key

                if i.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif i.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                encrypted += chr(num)
            else:
                encrypted += i
        print("Message is: ", encrypted)
        return encrypted


c = Caeser(mode, msg, key)
print(c)
print(c.checkMode())