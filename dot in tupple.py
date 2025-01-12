def dot(a, b, p):
    return tuple([x*y % p for x, y in zip(a, b)])
a = (1, 2, 3)
b = (1, 2, 3)

p = 5 

print(dot(a, b, p))