import sys

enc = sys.argv[1]

def findkey(enc):
    key = ""
    dec = bytes.fromhex(enc).decode()
    li = "THM{}"
    for i in range(0, 4):
        key += chr(ord(li[i]) ^ ord(dec[i]))
    key += chr(ord(li[-1]) ^ ord(dec[-1]))
    flag = ""
    for i in range(0, len(dec)):
        flag += chr(ord(dec[i]) ^ ord(key[i%5]))
    print("FLAG1:", flag) 
    print("KEY:", key)

findkey(enc)
