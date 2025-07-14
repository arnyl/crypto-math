from math import ceil, sqrt

def improved_baby_step_giant_step(h, g, p, max_exp=None):
    """
    Improved BSGS with better bounds and error handling
    """
    if max_exp is None:
        max_exp = p - 1
    
    if h == 1:
        return 0
    if h == g:
        return 1
    
    # Use smaller bound for efficiency
    m = min(int(ceil(sqrt(max_exp))), int(ceil(sqrt(p))))
    
    # Baby steps: store g^j for j = 0, 1, ..., m-1
    baby_steps = {}
    gamma = 1
    for j in range(m):
        if gamma == h:
            return j
        baby_steps[gamma] = j
        gamma = (gamma * g) % p
    
    # Giant steps: compute h * (g^(-m))^i for i = 0, 1, ..., ceil(max_exp/m)
    try:
        # Use extended Euclidean algorithm for modular inverse
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd_val, x, y = extended_gcd(pow(g, m, p), p)
        if gcd_val != 1:
            return None
        g_inv_m = x % p
        
    except:
        return None
    
    y_val = h
    max_i = min(m, int(ceil(max_exp / m)) + 1)
    
    for i in range(max_i):
        if y_val in baby_steps:
            result = i * m + baby_steps[y_val]
            if result <= max_exp:
                return result
        y_val = (y_val * g_inv_m) % p
    
    return None

def pollard_kangaroo(h, g, p, lower_bound=0, upper_bound=None):
    """
    Pollard's Kangaroo algorithm for bounded discrete logarithm
    Ideal for IPFE where we know the range of inner products
    """
    if upper_bound is None:
        upper_bound = p - 1
    
    if h == 1:
        return 0
    if h == g:
        return 1
    
    # Function for pseudo-random walk
    def f(x):
        return (x & 0x1F) + 1  # Simple function returning 1-32
    
    # Tame kangaroo starts at upper bound
    tame_pos = upper_bound
    tame_val = pow(g, tame_pos, p)
    
    # Wild kangaroo starts at target
    wild_pos = 0
    wild_val = h
    
    # Expected number of steps
    expected_steps = int(1.5 * sqrt(upper_bound - lower_bound))
    
    for step in range(expected_steps * 2):  # Safety factor
        # Move tame kangaroo
        jump = f(tame_val)
        tame_pos += jump
        tame_val = (tame_val * pow(g, jump, p)) % p
        
        # Move wild kangaroo  
        jump = f(wild_val)
        wild_pos += jump
        wild_val = (wild_val * pow(g, jump, p)) % p
        
        # Check for collision
        if tame_val == wild_val:
            result = tame_pos - wild_pos
            if lower_bound <= result <= upper_bound:
                return result
    
    return None


def solve_dlp(h, g, p, bound=None, verbose=False):
    """
    Solve for x in h ≡ g^x mod p using:
    - Brute force (if small bound)
    - Improved BSGS (if available)
    - Pollard's Kangaroo (bounded)
    
    Params:
        h: target value (int)
        g: generator (int)
        p: modulus (prime int)
        bound: optional max bound for x
        verbose: print which method is used
    
    Returns:
        x such that g^x ≡ h mod p, or None if not found
    """
    if h == 1:
        return 0
    if h == g:
        return 1

    order = p - 1
    max_bound = bound if bound is not None else order

    # Try brute force for small range
    if max_bound <= 1000:
        if verbose: print("[+] Using Brute Force")
        for x in range(max_bound + 1):
            if pow(g, x, p) == h:
                return x

    # Try improved BSGS
    if verbose: print("[+] Trying BSGS")
    result = improved_baby_step_giant_step(h, g, p, max_bound)
    if result is not None:
        return result

    # Try Pollard's Kangaroo
    if verbose: print("[+] Trying Pollard's Kangaroo")
    result = pollard_kangaroo(h, g, p, 0, max_bound)
    if result is not None:
        return result

    # Try negative values (if needed)
    if verbose: print("[+] Trying negative values")
    for x in range(1, max_bound + 1):
        if pow(g, (p - 1 - x) % (p - 1), p) == h:
            return -x

    return None

if __name__ == "__main__":
    p = int(input('p: '))
    g = int(input('g: '))
    h = int(input("Input h (g^x mod p): "))
    
    x = solve_dlp(h, g, p, bound=500, verbose=True)
    print(f"Computed x such that {g}^x ≡ {h} mod {p} is:\n=> x = {x}")
