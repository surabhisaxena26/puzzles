__author__ = 'surabhi'
def __findLonelyDigit(a):
    l=set()
    for j in a:
        if l.__contains__(j):
            l.remove(j)
        else:
            l.add(j)
    return l.pop()

n = int(raw_input())
arr = []
for i in range(0,n):
    arr.append(int(raw_input()))
print(__findLonelyDigit(arr))