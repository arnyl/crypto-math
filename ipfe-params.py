import random
import math
from math import gcd as bltin_gcd
from math import ceil, sqrt, floor

def rabinMiller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5): 
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: 
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = fast_exp(v, 2, num)
    return True

def isPrime(num):
    if (num < 2):
        return False 
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
                    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
                    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
                    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 
                    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 
                    509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 
                    613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
                    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 
                    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
                    919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabinMiller(num)

def gen_prime(keysize=5):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

def generators(n):
    required_set = {num for num in range(1, n) if bltin_gcd(num, n) }
    return [g for g in range(2, n) if required_set == {pow(g, powers, n)
            for powers in range(1, n)}]

def list_gen(p, l):
    random_list = []
    for i in range (0, l):
        x = random.randrange(2, p)
        random_list.append(x)
    return random_list

def fast_power(base, power):
    result = 1
    while power > 0:
        if power % 2 == 0:
            power = power // 2
            base = base * base
        else:
            power = power - 1
            result = result * base
            power = power // 2
            base = base * base
    return result

def setup(s, g):
    mpk = []
    for i in s:
        mpk.append((fast_power(g, i)))
    return mpk

def dot(a, b):
    return tuple([x*y for x, y in zip(a, b)])

def inn_product(a, b):
    return (sum(x*y for x, y in zip(a, b)))

def product(mylist) :
    result = 1
    for x in mylist:
         result = (result * x)
    return result

def comp_hr(mpk, r):
    temp = []
    for i in mpk:
        temp.append(fast_power(i, r))
    return temp

def comp_gx(g, x):
    temp = []
    for i in x:
        temp.append(fast_power(g, i))
    return temp

def log(x, b):
    if x < b:
        return 0
    return 1 + log(x//b, b)

def get_ctx(g, r, mpk, ptx):
    ct0 = fast_power(g, r)
    cti = dot(comp_hr(mpk, r), comp_gx(g, ptx))
    return (ct0, cti)

def get_data(g, y, sky, ct0, cti):
    cty = list(map(lambda n1, n2: fast_power(n1, n2), cti, y))
    cty_prod = product(cty)
    ct0_sky = fast_power(ct0, sky)
    ct_div = cty_prod//ct0_sky
    res = log(ct_div, g)
    return res
