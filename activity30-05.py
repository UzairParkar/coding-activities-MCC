#1

def ReorderedPower(n):
	return n
print(ReorderedPower(1))

#2

def StringNum(s):
	l = list(s)
	r = [] 
	total = 0
	for i in range(len(l)-1):
		if not l[i].isdigit():
			l[i] = ''
		elif l[i].isdigit() and l[i].isdigit():
			continue
		elif l[i].isdigit():
			continue
	for m in range(len(l)-1):
		if l[m].isdigit() and l[m+1].isdigit():
			r.append(''.join([l[m],l[m+1]]))
		elif l[m].isdigit() and not l[m+1].isdigit():
			r.append(l[m])
			
	for j in r:
		total += int(j)
	return total
	
print(StringNum('abc12xy34'))
print(StringNum('a1b2c3'))

#3

	
def is_valid_II(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
        left += 1
    return True

print(is_valid_II('abca'))
print(is_valid_II('racecar'))


#4
def RansomNote(ransomnote,magazine):
	ransomdict = {}
	magdict = {}
	ransomnote = list(ransomnote)
	magazine = list(magazine)
	for i in ransomnote:
		if i not in ransomdict:
			ransomdict[i] = 1
		else:
			ransomdict[i] += 1
	for j in magazine:
		if j not in magdict:
			magdict[j] = 1
		else:
			magdict[j] +=1
	vmag = list(ransomdict.items())
	vran = list(magdict.items())
	if vran in vmag:
		return True
	else:
		return False
	

print(RansomNote('aa','aab'))

#5
def SmallestNOD(d):
	return d
	
print(SmallestNOD('01-01-2023'))