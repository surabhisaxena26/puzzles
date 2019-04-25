__author__ = 'surabhi'
def __convert__alternating__chars (a):

    if len(a) < 2:
        return 0
    c = a[0]
    count = 0
    for i in range(1, len(a)):
        if a[i] == c:
            count += 1
        else:
            c = a[i]
    return count
n = int(raw_input())
b = []
for i in range(0,n):
    b.append(raw_input())
for i in range(0, n):
    print(__convert__alternating__chars(b[i]))





