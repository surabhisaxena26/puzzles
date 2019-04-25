__author__ = 'surabhi'
a = raw_input().split(' ')
n = a[0]  # size of array
d = int(a[1])  # diff
l = [int(x) for x in raw_input().split(' ')]
l.sort()
m = map(None, l)
count = 0
for i in l:
    if i+d in m:
        count += 1

print (count)

