"""
Integer Factorization Module
=============================
"""

from math import sqrt

def factorize(n):
    factors = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.add(n)
    return list(factors)

num = int(input('num: '))
factors = factorize(num)
print("Prime factors:", factors)