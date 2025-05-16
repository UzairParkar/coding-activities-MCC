#2 Count the pair of array whose sum is divisible by K



def CountPairs(arr,k):
	lst = []
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if arr[i] + arr[j] % k:
				temp = [i,j]
				if temp not in lst:
					lst.append(temp)
					temp = []
		return len(lst)
print(CountPairs([1,2,3,4,5,6],5))


#4 Staircase

def Staircase(n):
	for i in range(n+1):
		for j in range(i+1,n+1):
			print(" ",end=' ')
		for k in range(1,i+1):
			print("#",end=' ')

		print()


print(Staircase(6))

#3 Sort by frequency

def SortFreq(arr):
	lst = []
	dict1 = {}
	for i in arr:
		if i not in dict1:
			dict1[i] = 1
		else:
			dict1[i] += 1

	a = sorted(dict1.items())
	return a

print(SortFreq([4,4,1,2,2,2,3]))