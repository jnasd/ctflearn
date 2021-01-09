
import base64

comment2 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
comment3 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

plain2 = base64.b64decode(comment2)     # Unreadable
plain3 = base64.b64decode(comment3)     # Unreadable

i = 0
flag = ""
while (i < len(plain2)):
    ch1 = plain2[i]
    ch2 = plain3[i]
    xor = ord(ch1) ^ ord(ch2)
    flag += chr(xor)
    i += 1
print(flag)
