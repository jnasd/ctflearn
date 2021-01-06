import itertools


#define CTFDEBUG

def hashCode(value):
	h = 0
	if h == 0 or len(value) > 0:
		for i in range(0, len(value)):
			h = 31*h + ord(value[i])
	return h

# emunate for every possible combination, 'cobinations_with_replacement' will produce very
# lesser numbers of 'product',  sometimes, it saves time and succeed
# but this time, it will fail.
for x in itertools.combinations_with_replacement("0123456789abcdefghijklmnopqrstuvwxyz", 6):
    alice = "".join(x)
    if (not alice.isalpha()):
        if (not alice.isdigit()):
            hv = hashCode(alice)
            #ifdef(CTFDEBUG)
            if (hv < 1472550000 and hv > 1472540000):
                print("[debug info] " + str(alice) + " hashCode is: " + str(hv))
            #end
            if (hv == 1472541258):
                print("Succeed! I found the matched str: " + str(alice) + " hashCode is 1472541258")
                exit(0)

print("Failed! I can't find the matched str.")
