import random

def jacobi(a, n):
    if (n < 0) or (n % 2 == 0):
        return 0
    result = 1
    a = a % n
    while a != 0:
        while a % 2 == 0:
            a = a // 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0

def is_prime(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = jacobi(a, n)
        if x == 0 or pow(a, (n - 1) // 2, n) != (x % n):
            return False
    return True

def generate_prime_number(length=1024):
    while True:
        p = random.getrandbits(length)
        p |= (1 << length - 1) | 1
        if is_prime(p):
            return p

def mod_inverse(e, phi):
    # Extended Euclidean algorithm to find the inverse
    m0, x0, x1 = phi, 0, 1
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits):
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def rsa_encryption_demo():
    public, private = generate_keypair(1024)

    message = input("Enter a message to encrypt: ")
    cipher = encrypt(public, message)
    print("Encrypted message: ", cipher)

    decrypted_message = decrypt(private, cipher)
    print("Decrypted message: ", decrypted_message)

rsa_encryption_demo()
