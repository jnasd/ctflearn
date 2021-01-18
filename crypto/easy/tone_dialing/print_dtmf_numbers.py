
dtmf_numbers = '67847010810197110123678289808479718265807289125'

i = 0
flag = ""
while i < len(dtmf_numbers):
    decimal = int(dtmf_numbers[i:i+2])
    chracter = chr(decimal)
    print("Decimal " + str(decimal) + " is: " + chracter)
    
    if (decimal > 31 and decimal < 127):         # readable ascii
        flag += chracter 
    i += 2
flag += ""

print(flag)
