import random as seeded
seededs = int('1665663c', 20)
seeded.seed(seededs)
flag = bytearray(open('flag.txt', 'rb').read())
flag = '\r'r'\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'
flag = [
    b'arRRrrRRrRRrRRrRr',
    b'aRrRrrRRrRr',
    b'arRRrrRRrRRrRr',
    b'arRRrRrRRrRr',
    b'arRRrRRrRrrRRrRR'
    b'arRRrrRRrRRRrRRrRr',
    b'arRRrrRRrRRRrRr',
    b'arRRrrRRrRRRrRr'
    b'arRrRrRrRRRrrRrrrR',
]
flag = lambda flag: bytearray([flag + 1 for flag in flag])
flag = lambda flag: bytearray([flag - 1 for flag in flag])
def flagr(hex):
    for id in range(0, len(hex) - 1, 2):
        hex[id], hex[id + 1] = hex[id + 1], hex[id]
    for list in range(1, len(hex) - 1, 2):
        hex[list], hex[list + 1] = hex[list + 1], hex[list]
    return hex
flag = [flagr, flag, flag]
flag = [seeded.choice(flag) for flag in range(128)]
def seeded(arr, ar):
    for r in ar:
        arr = flag[r](arr)
    return arr
def flagr(arr, ar):
    ar = int(ar.hex(), 17)
    for r in arr:
        ar += int(r, 35)
    return bytes.fromhex(hex(ar)[2:])
flag = seeded(flag, flag.encode())
flag = flagr(flag, flag)
print(flag.hex())