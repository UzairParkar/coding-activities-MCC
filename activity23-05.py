print('Hello World')

#1. 

keypad = {1:'*',
2:['a','b','c'],
3:['d','e','f'],
4:['g','h','i'],
5:['j','k','l'],
6:['m','n','o'],
7:['p','q','r','s'],
8:['t','u','v'],
9:['w','z','x','z']}

dig = '23'
dig = list(dig)
s = ''
r = []
for ir in dig:
	for i,j in keypad.items():
		if ir == str(i):
			s += ''.join(j)

print(s)



	 



#2.
def is_automorphic(num):
	sqn = num*num
	strsq = str(sqn)
	char = len(str(num))
	if strsq.endswith(str(num)):
		return True
	else:
		return False	

print(is_automorphic(76))


#3.
keyboard = {
'row1':{'q','w','e','r','t','y','u','i','o','p'},
'row2':{'a','s','d','f','g','h','j','k','l'},
'row3':{'z','x','c','v','b','n','m'}
}
words = ['Hello','Alaska','Dad','Peace']
r = []
for i in words:
	w = i
	w = w.lower()
	if set(w).issubset(keyboard['row1']):
		row = keyboard['row1']
		r.append(i)

	if set(w).issubset(keyboard['row2']):
		row = keyboard['row2']
		r.append(i)


	if set(w).issubset(keyboard['row3']):
		row = keyboard['row3']
		r.append(i)

print(r)
			
		

#4.





#5.

def NextSmallestEven(arr):
	m = max(arr)
	if m % 2 == 0:
		arr.append(m+2)
	if m % 2 != 0:
		arr.append(m+1)
	return max(arr)

print(NextSmallestEven([3,2,6,1,8]))



