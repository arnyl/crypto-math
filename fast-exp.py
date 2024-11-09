'''
Here is the Fast Exponentiation Algorithm
:author: Arni Yulia
:date: 31-05-2022
'''

import math
import time

def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r


def main():
    b = 77578995801157823671636298847186723593814843845525223303932
    e = 121832886702415731577073962957377780195510499965398469843281
    m = 882564595536224140639625987659416029426239230804614613279163
    r = fast_exp(b, e, m)
    print("{} ^ {} ≡ {} (mod {})".format(b, e, r, m))

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'time : {end-start}')
