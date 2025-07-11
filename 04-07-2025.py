print('Hello World')

#1)

def determine_price(X,prices):
	bought = 0
	lst = []
	prices.sort()
	for i in prices:
		if bought != X:
			bought += i
			lst.append(i)
		return len(bought)
print(determine_price(60,[15,20,10,5,100,30]))
		
	

#2)

def remove_duplicates(d):
    s = set()
    for key in d:
        new_list = []
        for val in d[key]:
            if val not in s:
                new_list.append(val)
                s.add(val)
        d[key] = new_list
    return d

print(remove_duplicates({'Ravi':[2,3],'Sita':[3,4,5]}))

#3)

#4)

def count_rows(matrix):
	values = []
	for row in range(len(matrix)):
		values.append(len(matrix[row]))
	
	dict1 = dict(Counter(values))

	return dict1

print(count_rows([[6,3,1],[8,9],[2],[10,12,7],[4,11]]))

#5)  
from collections import Counter
def odd_frequency(M,nums):
	frequency = dict(Counter(nums))
	for i in frequency:
		if frequency[i] % 2 != 0:
			return i
print(odd_frequency(9,[4,5,6,4,6,6,5,4,4])) 
