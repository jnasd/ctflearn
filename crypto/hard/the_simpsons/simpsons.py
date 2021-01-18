# step 1: strings ItsKrumpint-Time.jpg
''' 
Ahh! Realistically the Simpsons would use octal instead of decimal!
encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051))
key = key + key + chr(ord(key)-4)
print(DecodeDat(key=key,text=encoded))
'''

# step 2: decode encoded and key
import math

encoded = '152 162 152 145 162 167 150 172 153 162 145 170 141 162'
key = '110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051'
encoded_list = encoded.split(' ')
key_list = key.split(' ')

encoded_str = ""
for i in encoded_list:
    decimal = int('0o' + i, 8)
    chracter = chr(decimal)
    encoded_str += chracter
print("The ciphertext is: " + encoded_str)


key_str = ""
for i in key_list:
    decimal = int('0o' + i, 8)
    chracter = chr(decimal)
    key_str += chracter
print(key_str)
''' key_str is: How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four) '''

# step 3: Google search 'Simpsons How much did Maggie originally cost'
# https://www.neatorama.com/2011/12/16/a-few-more-facts-about-the-simpsons, It shows Maggie originally cost $847.63
Maggie_cost = 847.63
SolutionToDis = math.ceil(Maggie_cost / 8) + 4           # 847.63 / 8 = 105.95375, SolutionToDis=110
key = chr(int(SolutionToDis))
key = key + key + chr(ord(key)-4)
print("The key is: " + key)


# step 4: decode ciphertext
# https://cryptii.com/pipes/vigenere-cipher, choose DECODE
# Ciphertext = jrjerwhzkrexar, key = nnj
# The flag is: wearenumberone
