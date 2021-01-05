import itertools

# Brute force to match the hashCode, needs about 100 seconds to running the program

#define CTFDEBUG

def hashCode(value):
	h = 0
	if h == 0 or len(value) > 0:
		for i in range(0, len(value)):
			h = 31*h + ord(value[i])
	return h

for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz", repeat=6):
    alice = "".join(x)
    if (not alice.isalpha()):
        if (not alice.isdigit()):
            hv = hashCode(alice)
            #ifdef(CTFDEBUG)
            if (hv < 1472600000 and hv > 1472500000):
                print("[debug info] " + str(alice) + " hashCode is: " + str(hv))
            #end
            if (hv == 1472541258):
                print("Succeed! I found the matched str: " + str(alice) + " hashCode is 1472541258")
                exit(0)
