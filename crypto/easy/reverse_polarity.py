

ciphertext = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"

count = len(ciphertext)
if (not(count % 8 == 0)):
    print("format of ciphertext is error, len is !" + str(count))
    exit(-1)

flag = ""
i = 0
while (i < count):
    byte_str = ciphertext[i:i+8]
    int_c = int(byte_str, 2)
    print(byte_str + ":" + str(int_c))
    if (int_c < 128):
        chracter = chr(int(byte_str, 2))
        flag += chracter
    i += 8
print(flag)
