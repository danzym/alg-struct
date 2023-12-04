def Legendre(arr, p):
    e = (p - 1) // 2
    results = [pow(a, e, p) for a in arr]
    return [(r-p if r > 1 else r) for r in results]

n = int(input("Enter a number for the Legendre function: "))
p = int(input("Enter a number for the Legendre function: "))
print("Legendre function for the number", n, "is equal to", Legendre([n], p))

def jacobi(a, m):
    if m <= 0:
        raise ValueError("m must be positive")
    if m % 2 == 0:
        raise ValueError("m must be odd")
    a %= m
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = m % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            result = -result
        a %= m
    if m == 1:
        return result
    else:
        return 0

a = int(input("Enter the value of a: "))
m = int(input("Enter the value of m: "))
print(jacobi(a, m))
