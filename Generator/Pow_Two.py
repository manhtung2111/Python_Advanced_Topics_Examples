def Powtwogen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


a = Powtwogen(5)
print(next(a))
for i in Powtwogen(5):
    print(i)