
# The first 4 characters: CTFL
# C - 1 = B; T + 1 = U; F + 1 = G; L + 1 = M;
# That's the point, if you're familiar with xor, you will know:
# A ascii character xor 0x1 will change one bit, so it's still another adjacent ascii character 

ciphertext = 'BUGMd sozc0o sx^0r^`vdr1ld|'

flag = ""
for i in ciphertext:
    flag += chr(ord(i) ^ 0x1)
print(flag)

# The output is:    CTFLe!rn{b1n!ry_1s_awes0me}
# But the flag is:  CTFLearn{b1nary_1s_awes0me}
