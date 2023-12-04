import random

def modpow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def legendre_symbol(a, p):
    return modpow(a, (p - 1) // 2, p)

def find_non_residue(p):
    for a in range(2, p):
        if legendre_symbol(a, p) == p - 1:
            return a
    return None

def cipolla_algorithm(n, p):
    if n == 0:
        return 0

    if legendre_symbol(n, p) == p - 1:
        return None

    while True:
        a = random.randint(0, p - 1)
        w = (a * a - n) % p
        if legendre_symbol(w, p) == p - 1:
            break

    u, v, k = a, 1, (p + 1) // 2
    x, y = 1, 0

    while k > 0:
        if k % 2 == 1:
            x, y = (x * u + y * v * w) % p, (x * v + y * u) % p
        u, v = (u * u + v * v * w) % p, 2 * u * v % p
        k = k // 2

    return min(x, p - x)

# Example usage
n = 8218   # The number for which to find the discrete square root
p = 10007  # A prime number satisfying the condition
root = cipolla_algorithm(n, p)
print(f"The discrete square root of {n} modulo {p} is {root}")
