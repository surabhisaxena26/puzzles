__author__ = 'surabhi'
def __is__panagram(a):
    b = [False for x in range(0,26)]
    # print(b)
    # print(str(a).strip(' ').lower())
    for x in str(a).lower():
        if x.isalpha():
            b[ord(x)-97] = True

    for i in range(0,26):
        if b[i] == False:
            return False

    return True
if __is__panagram(raw_input()):
    print("pangram")
else:
    print("not pangram")


