def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r

def power_List(a, c, d):
    list_b = []
    for i in a:
        b = fast_exp(c, i, d)
        list_b.append(b)
    return list_b

list_a = [61, 48, 4, 23, 54, 2, 22, 42]
print(power_List(list_a, 7, 71))

    


