def mod_inverse(a, m):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, y = extended_gcd(a % m, m)
        if gcd != 1:
            raise ValueError("Modular inverse does not exist")
        return x % m

a = int(input('a: ')) #integer elemen Z_m
m = int(input('m: ')) #modulus
x = mod_inverse(a, m)
print("modular inverse: ", x)
