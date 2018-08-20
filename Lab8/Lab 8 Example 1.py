class Celsius(object):
    def __init__(self, temperature=0):
        self._temperature = temperature
    def to_fahrenheit(self):
        return (self._temperature*9/5 + 32)
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, value):
        if value>=273:
            value=273
        self._temperature=value
    temperature = property(get_temperature, set_temperature)
    #print('temperature is', temperature)

c=Celsius()
print('c._temperature initially is ', c._temperature)
print('c.temperature is ', c.temperature)
c._temperature=32
print('\nCHANGE TO FAHRENHEIT')
print('c._temperature in celsius', c._temperature)
print('c.temperature is ', c.temperature)
print ('c._temperature in fahrenheit', c.to_fahrenheit())
c=Celsius(37)
print('\nGET TEMPERATURE')
print('c.get_temperature :', c.get_temperature())
print('c._temperature in celsius', c._temperature)
print('c.temperature is ', c.temperature)
c.set_temperature(39)
print('\nSET TEMPERATURE AT 39')
print('c._temperature is set to', c._temperature)
print('c.temperature is ', c.temperature)
c.set_temperature(390)
print('\nSET TEMPERATURE AT 390: IT WILL CHANGE TO 273')
print('c._temperature is set to', c._temperature)
print('c.temperature is ', c.temperature)








