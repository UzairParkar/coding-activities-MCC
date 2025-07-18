print('Hello World')



#1) 
def is_not_leap(year):
	if year % 4 !=0 and year % 100 == 0:
		return True
	if year % 100 != 0:
		return True
	else:
		return False

print(is_not_leap(2023))
print(is_not_leap(2019))


#2)
def is_divisible(num):
	c = 0
	s = str(num)
	for i in s:
		if int(i) == 0:
			continue
		if  int(i) % num:
			c +=1
			

	return c

print(is_divisible(111))
print(is_divisible(000))

#3)

def plus_one(num):
	Snum = str(num)
	temp = ''
	for i in Snum:
		if i.isdigit():
			temp += i

	n = int(temp) + 1
	res = []
	for i in str(n):
		res.append(int(i))			

	return res
print(plus_one([9,9,9]))

#4)


def generate_parenthesis(n):
	res = []
	def backtrack(open_count,close_count,path):
		if open_count == n and close_count == n:
			res.append(''.join(path))
			return 
		if open_count == 0:
			open_count = 1
			backtrack(open_count,close_count,'(')
		if close_count == 0:
			close_count += 1
			backtrack(open_count,close_count,')')
	backtrack(0,0,'')
	return res


print(generate_parenthesis(2))





#5)

def is_automorphic(num):
	snum = str(num)
	sqrt = str(num*num)
	print(sqrt[-len(snum):],snum)
	return sqrt[-len(snum):] == snum



print(is_automorphic(25))
print(is_automorphic(15))

























