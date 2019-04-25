__author__ = 'surabhi'
x = int(raw_input())
l = [int(i) for i in raw_input().split(' ')]
a = [None for j in range(0,100)]
for j in l:
    if a[j] == None:
        a[j] = True
    else:
        a[j] = False
for j in range(0,100):
    if a[j]==True:
        print(j)

