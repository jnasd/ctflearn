# python3 rsa_beginner.py

# borrow from libnum
# Extented Euclid GCD algorithm, returns (x, y, g) : a * x + b * y = gcd(a, b) = g
def xgcd(a, b):
    """
    Extented Euclid GCD algorithm.
    Return (x, y, g) : a * x + b * y = gcd(a, b) = g.
    """
    if a == 0: return 0, 1, b
    if b == 0: return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a

def invmod(a, n):
    """
    Return 1 / a (mod n).
    @a and @n must be co-primes.
    """
    if n < 2:
        raise ValueError("modulus must be greater than 1")

    x, y, g = xgcd(a, n)

    if g != 1:
        raise ValueError("no invmod for given @a and @n")
    else:
        return x % n

c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083
e = 1                   # plaintext is the same to cihpertext

# Method1: p,q from http://factordb.com/index.php
# Method2: In kali, factor n (spend over 1 hour, but no result...)
q = 416064700201658306196320137931
p = 590872612825179551336102196593

d = invmod(e, (p - 1) *(q - 1))
m = pow(c, d, n)

print(m)
print("hex is: " + hex(m))
plaintext = bytes.fromhex(hex(m)[2:])       # skip 0x of hex(m)
print(plaintext)


# Method2:
# plaintext = m.to_bytes(32, byteorder='big')
# print(plaintext)

# The flag is: abctf{b3tter_up_y0ur_e}
