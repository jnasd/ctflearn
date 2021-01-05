import itertools


def hashCode(value):
	h = 0
	if h == 0 or len(value) > 0:
		for i in range(0, len(value)):
			h = 31*h + ord(value[i])
	return h

# According the result of brute_force_lower.py, we find 0ghzxy matches the second condition
# We need another program to find the right str which matches both conditions
# conditions: 1) str.hashCode() == 1471587914  2) str.toLowerCase().hashCode() == 1472541258
for x in itertools.product("ghzxyGHZXY", repeat=5):
    bob = "".join(x)
    alice = '0' + bob
    if (not alice.isalpha()):
        if (not alice.isdigit()):
            hv = hashCode(alice)
            if (hv == 1471587914):
                print("Succeed! I found the matched str: " + str(alice) + " hashCode is 1472541258")
                exit(0)
