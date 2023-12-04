import random

a = random.randint(2, 10)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)


def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


def encrypt(msg, q, h, g):
    en_msg = []

    k = gen_key(q)  # Private key for sender
    s = pow(h, k, q)
    p = pow(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k: ", p)
    print("g^ak: ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p


def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = pow(p, key, q)
    for i in range(len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg


def elgamal_method():
    msg = input("Enter a message: ")

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    key = gen_key(q)
    h = pow(g, key, q)
    print("g = ", g)
    print("g^a  = ", h)

    en_msg, p = encrypt(msg, q, h, g)
    print("Encrypted message: ", en_msg)
    dr_msg = decrypt(en_msg, p, key, q)

    dmsg = ''.join(dr_msg)
    print("Decrypted message: ", dmsg);

elgamal_method()
