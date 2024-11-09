'''
Modular Inverse Algorithm
:author: Arni Yulia
:date: 31-05-2022
'''
from time import time

def mod_inv(a, m):
    for x in range(1, m):
        if ((( a % m) * (x % m)) % m == 1):
            return x
    return -1

start = time()
#for i in range (10):
    #a = mod_inv(13, 10733073986850449287)
end = time()
#print(a)
print(f'time: {end-start}')

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

start = time()
a = modinv(65537, 882564595536224140639625987659416029426239230804614613279163)
end = time()
print(a)
#print(f'time: {end-start}')







