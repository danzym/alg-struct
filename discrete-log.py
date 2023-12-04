import math

def discreteLogarithm(a, b, m):
    n = int(math.sqrt(m) + 1)

    # Check the base and modulus
    if a == 0 or m <= 1:
        return "Invalid input: a should be greater than 0 and m should be greater than 1."

    an = 1
    for i in range(n):
        an = (an * a) % m

    value = [0] * m

    cur = an
    for i in range(1, n + 1):
        if value[cur] == 0:
            value[cur] = i
        cur = (cur * an) % m

    cur = b
    for i in range(n + 1):
        if value[cur] > 0:
            ans = value[cur] * n - i
            if ans < m:
                return ans
        cur = (cur * a) % m

    return "Not found"

def babystep_giantstep_method():
    try:
        print("h = g^x mod p")
        h = int(input("h: "))
        g = int(input("g: "))
        p = int(input("p: "))

        if h < 0 or g < 0 or p < 0:
            print("All numbers should be non-negative.")
        else:
            result = discreteLogarithm(g, h, p)
            print("x = ", result)
    except ValueError:
        print("Invalid input.")

babystep_giantstep_method()
