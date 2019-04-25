x= int(raw_input())
s= raw_input().split(' ')[0:x]
print (s)
p,n,z=0,0,0
for y in s:
  #print("Iam here1")
  if int(y)>0:
    #print("Iam here2")
    p=p+1
  elif int(y)<0:
    n=n+1
  else:
    #print("Iam here3")
    z=z+1
print(p,n,z)
print ("%.3f" % (float(p)/x))
print ("%.3f" % (float(n)/x))
print ("%.3f" % (float(z)/x))




