print('Hello World')

#2

def MaximumNumeric(s):
	s = list(s)
	num = ''
	numbers = []
	for i in range(len(s)):
		if not s[i].isdigit():
			s[i] = ''
		else:
			num += s[i]
			if not s[i+1].isdigit():
				numbers.append(int(num))
				num = ''
	return max(numbers)

print(MaximumNumeric('100klh564abc365bg'))


#3
def IfPair(arr,x):
	collection = {arr[i]:i for i in range(len(arr))}
	
	for i in collection:
		if x-i in collection:
			# why? because 16 - 6 == 10 and 10 + 6 == 16
			return True
print(IfPair([1,4,45,6,10,8],16))

#4
# have to check if total amount of goods 15 in this case can be redistributed on the basis of i 1+2+3+4+5 = 12
def Distribute(n,goods):
	sgoods = sum(goods)
	res = []
	for i in range(len(goods)):
		print(i,goods.index(goods[i]),goods[i])
		if i in res:
			i = goods.index(goods[i]) + 1
			print(i)
			res.append(i)
		else:
			i = goods.index(goods[i]) + 1
			res.append(i)

	if sgoods == sum(res):
		return True
	else:
		print(res)
		print(sum(res))
		return False
		
print(Distribute(5,[7,4,1,1,2]))



#1	
def Flatten(lst):
	res = {}
	for i in lst:
		res = lst		



print(Flatten({'a':1,'b':{'c':2,'d':{'e':3,'f':4}}}))
	

