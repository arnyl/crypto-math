space = 2**16

def xor(a, b):
    new = int(a, 2) ^ int(b, 2)
    return '{0:016b}'.format(new)

def mod_add(a, b):
    new = (int(a, 2) + int(b, 2)) % space
    return '{0:016b}'.format(new)

def inv_add(k):
    inv = space - k
    return inv

def mod_mul(a, b):
    new = (int(a, 2) + int(b, 2)) % space
    return '{0:016b}'.format(new)

def inv_mul(a):
    m = space + 1
    g = gcd (a, m)
    if g != 1:
        raise Exception('tidak ada invers')
    else:
        return power (a, m - 2, m)

def gcd(a, b):
    if a == 0:
        return b
    return gcd (b % a, a)

def power(x, y, m):       
    if y == 0: 
        return 1       
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
    if y % 2 == 0: 
        return p  
    else :  
        return ((x * p) % m) 

def split(x):
    n = 16
    block = [x [i:i+n] for i in range (0, len(x), n)]
    return block

def left_shift(bits):
    temp = 25 % len(bits)
    res = bits[temp: ] + bits[ : temp]
    return res

def keygen(bits):
    if len(bits) != 128:
        raise Exception('ukuran input tidak memenuhi')
    key = []
    for i in range (7):
        subkey = split(bits)
        key += subkey
        bits = left_shift(bits)
    return key[:-4]





key = '00010101111010110010001011001111110000010110001011011001100000000100101010010110001001001000100000100100010000001111111110100100'
plain = '1111000100101001101001100110000000011110111101100010101001000111'


#print(split(a, 16))
#print(left_shift(a))
list_1 = keygen(key)
print(len(list_1))
