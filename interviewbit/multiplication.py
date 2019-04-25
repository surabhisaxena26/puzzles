# Implement multiplication of two string integers

class Solution:

	def to_number(self,x):
		j=0
		for i in reversed(range(0,len(x))):
			j+=(ord(x[i])-48)*(10**(len(x)-1-i))
		return j

	def sanitize(self,x):
		trimmed= x.strip()
		if trimmed[0] in {'+','-'}:
			return (-1 if trimmed[0]=='-' else 1,trimmed[1:].strip())
		else:
			return (1,trimmed)
		

	def multiply(self, a1,b1):
		result_a,result_b = self.sanitize(a1),self.sanitize(b1)
		print(result_a)
		print(result_b)
		a,b = result_a[1], result_b[1]
		small= a if len(a)<len(b) else b
		large= b if len(a)<len(b) else a
		result=0
		for i in reversed(range(0,len(small))):
			carry=0
			multiplier= self.to_number(small[i])
			k=""
			for j in reversed(range(0,len(large))):
				actual_sum= carry+ multiplier*self.to_number(large[j])
				k+=str(actual_sum%10)
				carry=actual_sum//10
			if carry>0:
				k+=str(carry)
			print(k)
			result+=self.to_number(k[::-1])*(10**(len(small)-1-i))
			print ("toadd "+str(self.to_number(k[::-1])*(10**(len(small)-1-i))))
			print("result="+ str(result))
		return str(result*result_a[0]*result_b[0])

app = Solution()
# print(str(app.multiply('19','5')))
# print(str(app.multiply('19','05')))
# print(str(app.multiply('19','00005')))
# print(str(app.multiply('10','111')))
print(str(app.multiply('99999','99999')))
#print(str(app.multiply(' - 10 ',' - 111')))
