class InfInter:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

i = iter(InfInter())
print(next(i))
print(next(i))
print('')
