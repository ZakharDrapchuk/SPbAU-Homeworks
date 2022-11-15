import math

iter = 20

def my_expo(x):
    x_pow = x
    mult = 1
    part_sum = 0
    for n in range (0, iter):
        x_pow = x**n
        if n == 0:
            mult = 1
        else:     
            mult *= 1 / (n)
        part_sum +=  x_pow * mult
    return part_sum
help(math.exp)
help(my_expo)

print(math.exp(0.3))
print(my_expo(0.3))
