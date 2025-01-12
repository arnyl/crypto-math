from time import time
from math import gcd as bltin_gcd


def primRoots(n):
    required_set = {num for num in range(1, n) if bltin_gcd(num, n) }
    return [g for g in range(1, n) if required_set == {pow(g, powers, n)
            for powers in range(1, n)}]
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
"""
def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots
"""


    
start2 = time()
print('running ...')
print(primRoots(11))
end2= time()
print(f'waktu: {end2-start2} ')