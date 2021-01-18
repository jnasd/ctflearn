
import base64

flag_file = open('flag.txt', 'r')
ciphertext = flag_file.readline()
#print(ciphertext)

cipher = ciphertext
i = 0
while 1:
    plaintext = base64.b64decode(cipher)
    if (plaintext.find('{') != -1 and plaintext.find('CTF') != -1):
        print(plaintext)
        print(i)
        exit(0)
    cipher = plaintext
    i += 1
