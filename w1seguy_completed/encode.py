import random
import string

flag = 'THM{thisisafakeflag}' 
def encode():
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    key = str(res)
    print("FLAG:", flag)
    print("KEY:", key)
    xored = ""

    for i in range(0,len(flag)):
        xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))
    
    print("XOR:", "chr(ord(flag[i]) ^ ord(key[i%len(key)]))")
    hex_encoded = xored.encode().hex()
    return hex_encoded

enc = encode()
print("ENCODED:", enc)
