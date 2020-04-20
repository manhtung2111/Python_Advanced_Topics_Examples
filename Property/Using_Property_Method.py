# private method là __
# https://www.geeksforgeeks.org/underscore-_-python/
class Alphabet:
    def __init__(self, value):
        self._value = value

    def getValue(self):
        print('Getting value...')
        return self._value

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

    def delValue(self):
        print('Deleting value')
        del self._value




    value = property(getValue, setValue,delValue )


x = Alphabet('NgoManhTung')
print(x.value)
x.value = 'Ngo'
del x.value


