import itertools
import hashlib

 
def md5(para1):
    m = hashlib.md5()
    m.update(para1.encode("utf8"))
    return m.hexdigest()



'''
for x in itertools.product("BJMSabehiklor", repeat=5):
    alice = "".join(x)
    md = md5(alice)
    if (md == 'bafa3de6dac066cebe8c0e5670d98935'):
        print("The flag is: " + alice)
'''  

# https://md5.gromweb.com/
flag = 'CTF{MD5_is_Nasty}'
print(md5(flag))
