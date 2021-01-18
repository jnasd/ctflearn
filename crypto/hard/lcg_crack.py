'''
1. Learn the rules of modulus operation
   rule1: (a + b) % p = (a % p + b % p) % p
   rule2: (a - b) % p = (a % p - b % p) % p
   rule3: (a * b) % p = (a % p * b % p) % p
   rule4: (a ^ b) % p = ((a % p) ^ b) % p

2. use the modulus rules to derivation lcg
   x2 = (a * x1 + c) mod m
   x3 = (a * x2 + c) mod m
   
   x3 - x2 = [(a * x2 + c) mod m] - [(a * x1 + c) mod m]
   use rule 2:
   (x3 - x2) mod m = {[(a * x2 + c) mod m] - [(a * x1 + c) mod m]} mod m
                   = [(a * x2 + c) - (a * x1 + c)] mod m
                   = (a * x2 - a * x1) mod m
                   = (a * (x2 - x1)) mod m

3. wo can easily compute the left equality: (x3 - x2) mod m
   left = (x3 - x2) mod m
   delta = x2 - x1
   left = (a * delta) mod m
   => a * delta = left + k * m
   => a = (left + k * m) // delta
      so bruteforce the a (set k = 0, 1, 2, 3, 4...)
'''

def prng_lcg(multiplier, increment, modulus, x_n):
    x_next = (multiplier * x_n + increment) % modulus
    return x_next

def crack_c(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return increment

def crack_a(states, modulus):
    left = (states[2] - states[1]) % modulus
    delta = states[1] - states[0]
    k = 0
    while True:
        tries = left + modulus * k
        if (tries % delta == 0):                         # if (left + k * m) is divided by delta with no remainder, then we find it.
            multiplier = tries // delta
            return multiplier
        k += 1

xn = [65001687610455615650, 880901038222735, 16032398895653777]
m = 121409833232633162281
a = crack_a(xn, m)
c = crack_c(xn, m, a)
print("a = " + str(a) + ", c = " + str(c))

x3 = prng_lcg(a, c, m, 16032398895653777)
x3 = str(x3)

i = 0
flag = "CTFlearn{"
while i < len(x3):
    flag += chr(int(x3[i:i+2]))
    i += 2
flag += "}"
print(flag)



''' For test '''
#print(crack_a([2, 4, 1], 9))             # a = 3, c = 7, mod = 9
#print(crack_a([8, 14, 0], 17))           # a = 9, c = 27, mod = 17
