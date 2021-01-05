import itertools

# After 3 hour's, It's still running, the result not appear!!!
# The complexis is too large...

def hashCode(value):
	h = 0
	if h == 0 or len(value) > 0:
		for i in range(0, len(value)):
			h = 31*h + ord(value[i])
	return h

for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz",repeat=6):
    alice = "".join(x)
    if (not alice.isalpha()):
        hv = hashCode(alice)
        print(str(alice) + " 's hashCode is: " + str(hv))
        if (hv == 1472541258):
            exit(0)
