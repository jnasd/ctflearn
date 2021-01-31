

fd = open('TheMessage.txt', 'r').read()

result = ""
for char in fd:
    #print(ord(char))
    if (ord(char) == 0x20):
        result += "0"
    elif (ord(char) == 0x8f):        # e2 80 8f
        result += "1"

print(result)
