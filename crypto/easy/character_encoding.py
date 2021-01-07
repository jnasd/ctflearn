
str_num = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
list_num = str_num.split()

flag = ""
for i in list_num:
    flag += chr(int(i, 16))
    
print(flag)