import itertools


def hashCode(value):
	h = 0
	if h == 0 or len(value) > 0:
		for i in range(0, len(value)):
			h = 31*h + ord(value[i])
	return h
    
# emunate every possible combination.
    
#for x in itertools.combinations_with_replacement('0123456789abcdefghijklmnopqrstuvwxyz', 6):
for x in itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyz0123456789', 6):
    alice = "".join(x)
    if (not alice.isalpha()):
        if (not alice.isdigit()):
            hv = hashCode(alice)
            print(str(alice) + " 's hashCode is: " + str(hv))
            if (hv == 1472541258):
                exit(0)
