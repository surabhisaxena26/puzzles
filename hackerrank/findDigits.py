__author__ = 'surabhi'
def __count_digits(n):

    count = 0
    g = n
    while n > 0:
        r = n%10
        if r != 0 and 0 == g%r:
            count+=1
        n /= 10
    return count


t = int(raw_input())
n = []
for i in range(0,t):
    n.append(int(raw_input()))
for x in n:
    print(__count_digits(x))