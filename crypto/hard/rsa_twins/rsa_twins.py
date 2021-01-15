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

c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587
n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
e = 65537 

# Method1: p,q from http://factordb.com/index.php
# Method2: In kali, factor n (spend over 1 hour, but no result...)
q = 121588253559534573498320028934517990374721243335397811413129137253981502291629
p = 121588253559534573498320028934517990374721243335397811413129137253981502291631
d = invmod(e, (p - 1) *(q - 1))
m = pow(c, d, n)

print(m)
print("hex is: " + hex(m))
plaintext = bytes.fromhex(hex(m)[2:])       # skip 0x of hex(m)
print(plaintext)


# Method2:
# plaintext = m.to_bytes(32, byteorder='big')
# print(plaintext)

# The flag is: abctf{rs4_is_aw3s0m3}
