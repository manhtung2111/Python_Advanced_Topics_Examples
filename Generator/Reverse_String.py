def rev_str(my_str):
    length = len(my_str)
    for i in range (length - 1, -1, -1): # đếm ngược từ len - 1 tới 0 theo chiều giảm dần
        yield my_str[i]
a = rev_str('Hello')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print("------------------")
for i in rev_str('Hello'):
    print(i)
print('')
a = 'Heloo'

print(a[3])