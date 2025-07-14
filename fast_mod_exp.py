def fast_exp(base, exponent, modulus):
    result = 1
    base = base % modulus  # reduce base first

    while exponent > 0:
        if exponent % 2 == 1:         # if exponent is odd
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2      # divide exponent by 2

    return result

g = int(input('g: ')) #base
x = int(input('x: ' )) #exponent
m = int(input('m: ')) #modulus

print('result:', fast_exp(g, x, m))