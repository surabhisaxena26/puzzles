'''
Array consist of -1 and 1, Find count of all sub-arrays where sum = 0. 
https://careercup.com/question?id=5750115626123264 
'''
# returns count of subarrays whose sum is equal to the given constant
def count_sub_arrays(arr,constant):
	count=0
	temp=[]
	for i in range(0,len(arr)):
		for j in range(0,i):
			temp[j]+=arr[i]
		temp.append(arr[i])
		count+=len(list(filter(lambda x: x==0, temp)))
	return count

print(count_sub_arrays([1,-1,1],0))
print(count_sub_arrays([1,-1,-1,1,-1,-1,1],0))
