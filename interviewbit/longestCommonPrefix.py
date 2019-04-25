# https://www.interviewbit.com/problems/longest-common-prefix/

class Solution:

	def find_common_prefix(self,strings):
		result=""
		i=0
		prefix_match=True
		while prefix_match:
			k=""
			for string in strings:
				if i>=len(string):
					prefix_match=False
					break
				if len(k)==0 :
					k=string[i]
				elif k!= string[i]:
					prefix_match=False
					break
			if prefix_match:
				result+=k
			i+=1
		return result

app = Solution()
print(app.find_common_prefix(['abcdef','abcdj']))