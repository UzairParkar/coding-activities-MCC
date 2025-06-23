

#1 
print('Question 1')
def POWFour(n):
	powers = [4**i for i in range(0,50)]
	#print(powers)
	if n in powers:
		return True
	else:
		return False 
print(POWFour(16))
print(POWFour(5))


#2 Morse Code
print('Question 2')
def UniqueMorse(arr):
	morse_code = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 	'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 	'x':'-..-', 'y':'-.--', 'z':'--..'}
	unique = []
	for key,values in morse_code.items():
		for i in arr:
			pass 
			

print(UniqueMorse(['gin','zen','gig','msg']))






print('Question 3')
#3
def GreatestRightSide(arr):
	max_last = -1
	for i in range(len(arr)-1,-1,-1):
		current = arr[i]
		arr[i] = max_last
		max_last = max(max_last,current)
	return arr
print(GreatestRightSide([17,18,5,4,6,1]))
print(GreatestRightSide([400]))


#4 if any permutation of s1 appears as a substring
print('Question 4')
def PermutationsS1(s1,s2):
	arr = list(s2)
	arr = sorted(arr)
	tl = []
	temp = ''
	for i in range(len(arr)):	
		temp += arr[i]
		if len(temp) == len(s1):
			tl.append(temp)
			temp = ''
	for j in tl:
		if j == s1:
			return True
		

print(PermutationsS1('ab','eidbaooo'))
print(PermutationsS1('ab','eidboaoo'))	

print('Question 5')
#5 count trailing zeros
def factorial(f):
	if f == 0:
		return 1
	else:
		return f * factorial(f-1)

def CountTrailing(f):
	count = 0 
	num = factorial(f)
	# print(num,'-number')
	lnum = list(str(num))
	# print(lnum,'the list')
	for i in range(len(lnum)-1,-1,-1):
		if lnum[i] != '0':
			break
		else:
			count +=1
	return count 

print(CountTrailing(5))
print(CountTrailing(100))
	