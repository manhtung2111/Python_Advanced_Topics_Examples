# Closure : khep kin
# dung trong vong lap long nhau

def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(4))
print(times5(5))
