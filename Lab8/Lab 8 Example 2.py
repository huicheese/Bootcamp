class Time(object):
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    def get_elapsed_time(self):
        return self._hours * 60 * 60 + self._minutes * 60 + self._seconds
    def set_elapsed_time(self, seconds):
        overflow = seconds % (24 * 60 * 60)
        self._hours = overflow / (60 * 60)
        remainder = overflow % (60 * 60)
        self._minutes = remainder / 60
        self._seconds = remainder % 60
    elapsed_time=property(get_elapsed_time,set_elapsed_time)
    def __str__(self):
        return "Time: %d:%d:%d"%(self._hours, self._minutes, self._seconds)

t=Time(10,19,10)
print(t)
print(t.get_elapsed_time())
t.set_elapsed_time(500)
print('__str__')
print(t.__str__())
