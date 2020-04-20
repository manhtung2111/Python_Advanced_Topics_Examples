my_list = [5, 6, 8, 9]

my_iter = iter(my_list)



try:
    print(next(my_iter))

    print(next(my_iter))

    print(my_iter.__next__())

    print(my_iter.__next__())

    next(my_iter)
except StopIteration:
    print("Out of list")


print(next(my_iter))

print(next(my_iter))

print(my_iter.__next__())

print(my_iter.__next__())

next(my_iter)
