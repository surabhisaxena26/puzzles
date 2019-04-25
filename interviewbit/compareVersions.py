# compare two versions, v1>v2 return 1,0,-1
class Solution:
	def to_number(self,x):
		j=0
		for i in reversed(range(0,len(x))):
			j+=(ord(x[i])-48)*(10**(len(x)-1-i))
		return j

	def split(self, x):
		if len(x)==0:
			return (-1,0,-1)
		split_x=x.find('.')
		if split_x > -1 :
			return (split_x,self.to_number(x[:split_x]),x.find('.',split_x) if split_x!=-1 else -1)
		else :
			return (-1,self.to_number(x),-1)
		
	def compareVersion(self,v1, v2):
		res_x=self.split(v1)
		res_y=self.split(v2)
		if res_x[1] < res_y[1]:
			return -1
		elif res_x[1] > res_y[1]:
			return 1
		elif res_x[2]==-1 and res_y[2]==-1:
				return 0
		else:
			next_x = v1[res_x[2]+1:] if res_x[2] >-1 else ''		
			next_y = v2[res_y[2]+1:] if res_y[2] >-1 else ''
			return self.compareVersion(next_x,next_y)

app = Solution()
print(str(app.compareVersion('0.1','0.2')))
print(str(app.compareVersion('0.0','0.5.0')))
print(str(app.compareVersion('01.1','0.2')))
print(str(app.compareVersion('13.0','13.0.8')))