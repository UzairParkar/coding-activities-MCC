#1

def MovingZeros(arr):
     for i in range(len(arr)):
          for j in range(len(arr)-1):
               if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
     return arr
print(MovingZeros([0,1,0,3,12]))

#2 

def permutations(s):
     lst = []
     a = s
     a = ''.join(sorted(a))
     if a not in lst:
          lst.append(a)
          if a in lst:
             a = a[::-1]
             lst.append(a)
     
     a = s[-1:] + s[:-1]
     lst.append(a)
     if a not in lst:
          a = a[::-1]
          lst.append(a)
     
     for j in lst:
         if j in lst:
            j = j[-1:] + j[:-1]
            if j not in lst:
                lst.append(j)
     lst = sorted(lst)          
     return lst
     
print(permutations('abc'))



#3 
def CheckToplitz(matrix):
     return matrix
print(CheckToplitz([[1,2,3,4],[8,1,2,3],[9,5,1,2]]))






