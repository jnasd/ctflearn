#!/bin/python3

file = open('field.txt', 'r')

line = file.readline()

i = 0
xor_index = 0
add_index = 0
binary = 0
while i < len(line):
    polynomial = line[i:]
    #print(polynomial)
    xor_index = polynomial.find('x^')
    if (xor_index != -1):
        add_index = polynomial.find(' +')
        j = polynomial[xor_index+2:add_index]
        curr = 1 << int(j)
        binary = binary | curr
        #print(j)
    else:
        if (polynomial.find('1') != -1):
            binary = binary | 1
    i += (add_index + 2)

print(bin(binary))
flag = bytes.fromhex(hex(binary)[2:])       # skip 0x of hex(binary)
print(flag)

# The flag is: flag{p0lynom1als_4r3_k00l}
