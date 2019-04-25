'''
Problem : https://www.interviewbit.com/problems/atoi/
'''
def atoi(s):
    is_negative=False
    val="";
    for k in s:
        if ord(k)==45 and len(val)==0:
            is_negative=True
            continue
        elif ord(k) == 43 and len(val) == 0:
            continue
        elif ord(k) == 32 and len(val)==0:
            continue
        elif ord(k) > 47 and ord(k) < 58:
            val += k
        else:
            break

    number=0
    #print("Number is "+str(val))
    for i in reversed(range(0,len(val))):
         number+=(ord(val[i])-48)*(10**(len(val)-1-i))

    if is_negative:
        return -1*number
    else:
        return number


print(atoi("45"))
print(atoi("+45"))
print(atoi("-45"))
print(atoi("-45 189"))
print(atoi("- 45 189"))
print(atoi("- 45 189asdsdsd"))
print(atoi("-ad 45 189asdsdsd"))
print(atoi("9 2704"))
print(atoi("01 2704"))
print(atoi("- 01 2704"))
print(atoi(" +01 2704"))
print(atoi("- 5 88C340185Q  71  8079 834617385 2898422X5297Z6900"))