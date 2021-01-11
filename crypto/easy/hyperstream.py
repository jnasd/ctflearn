
# The Baconian cipher is a substitution cipher in which each letter is replaced by a sequence of 5 characters

ciphertext = 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB'

i = 0
cipher_pre = ""
while (i < len(ciphertext)):
    cipher_pre += ciphertext[i:i+5]
    cipher_pre += " "                   # Add space as split per 5 characters
    i += 5
print(cipher_pre)

# use   https://cryptii.com/pipes/bacon-cipher
# flag is: ilouebacondontyou
