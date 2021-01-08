

ciphertext = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

# use python's dictionary is more proper
# ch_to_num = {'!':1, '@':2, '#':3, '$':4, '%':5, '^':6, '&':7, '*':8, '(':9, ')':0}
# for ch in cihpertext:
#     if ch in ch_to_num:
#         cihper_mediate += str(ch_to_num[ch])

cipher_mediate = ""
for i in ciphertext:
    if (i == '!'):
        cipher_mediate += '1'
    elif (i == '@'):
        cipher_mediate += '2'
    elif (i == '#'):
        cipher_mediate += '3'
    elif (i == '$'):
        cipher_mediate += '4'
    elif (i == '%'):
        cipher_mediate += '5'
    elif (i == '^'):
        cipher_mediate += '6'
    elif (i == '&'):
        cipher_mediate += '7'
    elif (i == '*'):
        cipher_mediate += '8'
    elif (i == '('):
        cipher_mediate += '9'
    elif (i == ','):
        cipher_mediate += ','
    elif (i == ')'):
        cipher_mediate += '0'
    else:
        print("wrong character!" + str(i))
print(cipher_mediate)
cipher_list = cipher_mediate.split(',')
flag = ""
for i in cipher_list:
    flag += chr(int(i))
print(flag)
