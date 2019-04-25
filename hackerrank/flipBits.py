__author__ = 'surabhi'

def __flip_bits(a):
    s = bin(a)[2:]
    # print(s)
    k = [0]*32
    i = [1]*32
    r = [0]*32
    # print(k)
    # print (i)
    for x in range(0,len(s)):
        k[31-x]=int(s[len(s)-1-x])
    for x in range(0,32):
        r[x] = k[x] ^ i[x]

    return int(''.join( str(x) for x in r),2)

n = int(raw_input())
arr = []
for i in range(0,n):
    arr.append(int(raw_input()))

for i in range(0,n):
    print (__flip_bits(arr[i]))


