n=int(raw_input())
d={}
for i in range(0,n):
    b=raw_input()
    tokens= b.split(' ')
    #print (tokens)
    #print (tokens[1:4])
    c=b.split(' ')[1:4]
    d[tokens[0]]=sum([float(x) for x in c])/3
print("%.2f" % d[raw_input()])
