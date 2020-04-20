class Alphabet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print('Getting value')
        return self._value

    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value


x = Alphabet('Hello')
print(x.value)
x.value = 'Good morning'
