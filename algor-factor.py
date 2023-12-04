import random
import math

def modpow(base, exponent, modulus):
    res = 1

    while (exponent > 0):
        if (exponent & 1):
            res = (res * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return res

def pollard(n):
    # Handling special cases
    if (n == 1):
        return n
    if (n % 2 == 0):
        return 2

    # Initialize variables x, y, c
    x = random.randint(0, 2) % (n - 2)
    y = x
    c = random.randint(0, 1) % (n - 1)

    # Initialize divisor
    d = 1

    # Loop until a divisor is found
    while (d == 1):
        # "Tortoise" (slow step)
        x = (modpow(x, 2, n) + c + n) % n

        # "Hare" (fast step)
        y = (modpow(y, 2, n) + c + n) % n
        y = (modpow(y, 2, n) + c + n) % n

        # Calculate the greatest common divisor
        d = math.gcd(abs(x - y), n)

        # If d equals n, try again
        if (d == n):
            return pollard(n)

    # Return the divisor
    return d

# Read the number to factorize
check = int(input("Enter a number for factorization: "))

# Display the result
print("Result: ", check, " : ", pollard(check))
