
##### Method 1:
# 密文中每个字符（ascii）占 1 个字节, key 从 0x00 -> 0xff 时，刚好每个字符与key长度一致
# eg.  bin(ord('q')) = '0b1110001' ^ key = 0x1('0b00000001') = '0b1110000' ('p')
# 如果 key 超过 0xff, 那么需要特殊处理（将ciphertext全部转换为二进制位串)，每次选择和key位数相同的位串，与 key 进行 xor

##### Method 2:
# 1. use cyberchef:  https://www.chinabaiker.com
# 2. choose  XOR Brute Force
# 3. Input :  q{vpln'bH_varHuebcrqxetrHOXEjgwox{RgqssihYspOntqpxs}
# 4. watch the result (if contains some keywords like ctf, CTF, or Flag, flag...)
# 5. we can accelerate it, use keywords(flag) to fill Crib(known plaintext string)

ciphertext = "q{vpln'bH_varHuebcrqxetrHOXEjgwox{RgqssihYspOntqpxs}"

for key in range(64):
    flag = ""
    for i in ciphertext:
        charac = chr(ord(i) ^ key)
        flag += charac
    print("key = " + str(key) + ": " + flag)

# when key = 23, flag is: flag{y0u_Have_bruteforce_XOR} 
