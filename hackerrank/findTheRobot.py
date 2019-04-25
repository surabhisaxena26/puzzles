__author__ = 'surabhi'
def __find_robot(a):
    x,y = 0,0
    for i in range(0,len(a)):
        g=divmod(i,2)
        if g[1] == 0:
            if g[0]%2 == 0:
                x+=a[i]
            else:
                x-=a[i]
        else:
            if g[0]%2 == 0:
                y+=a[i]
            else:
                y-=a[i]
        print ('%d %d' %(x,y))
    return [x,y]
t= int(raw_input())
a=[]
for i in range(0,t):
    a.append(int(raw_input()))
c = __find_robot(a)
# print ('%d %d' %(c[0],c[1]))



