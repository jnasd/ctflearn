
reverse_str = "d733432373937303734373666343730373937323733343b7644534"
flag_hex = reverse_str[::-1]   # reverse it

flag = ""

i = 0
while (i < len(flag_hex)):
    print(flag_hex[i:i+2])
    chracter = int(flag_hex[i:i+2], 16)
    flag += chr(chracter)
    i += 2
print(flag)