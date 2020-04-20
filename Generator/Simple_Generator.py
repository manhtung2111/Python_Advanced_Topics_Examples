def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
for i in my_gen():
    print(i)
print('-------------------------')
print(next(a))
print(next(a))
print(next(a))
try:
    print(next(a))
except StopIteration:
    print('Cant print more')
