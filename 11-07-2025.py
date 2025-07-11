print('Hello World')

#1)
#2)
from collections import Counter
def k_frequent(nums,k):
	freq = Counter(nums)
	f  = freq.items()
	s = sorted(f,key=lambda x : -x[1])
	print(s)
	return [i[0] for i in s[:k]]

print(k_frequent([4,4,4,6,6,7,8],2))	

#3) 



#4)
def pascal_triangle(n):
	for i in range(1,n+1):
		print((n-i),end=" ")
		for j in range(1,i-1):
			print(j,end=" ")
		print()

print(pascal_triangle(6))
			
			


#5)
def increasing_number(n):
	for i in range(n):
		val = 1
		print(" " * (i-n),end='')
		for j in range(i):
			print(val,end='')
			val = val + 1
		print()

print(increasing_number(6))