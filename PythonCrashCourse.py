#int 
print("--ints")
a = 2
print(a, type(a))
a += 1 #equivalent to a = a + 1 (python does not have a ++ operator)
print(a, type(a))
a *= 2 #equivalent to a = a * 2
print(a, type(a))

#float
print("--floats")
b = 1.
print(b, type(b))
b = 1.5
print(b, type(b))

#Booleans
print("--booleans")
a = True
b = False

print(type(a))
print(a and b) #note that all logical operators (other than xor) are words and not symbols
print(a or b) 
print(not a)
print(a != b)

#if else Statements
print("--if else")
mark = 79

if mark >= 85:
    grade = "HD"
elif mark >= 75: #"else if" is abbreviated to "elif"
    grade = "D"
elif mark >= 65:
    grade = "C"
elif mark >= 50:
    grade = "P"
else:
    grade = "F"
    
print(grade)

#string concatination
print("--string concatination")
a = "compupter"
b = "1234567"
a += b #string concatenation

print(a)

print(len(a)) #length
print(a, type(a))
print(a[0]) #access the 0th (first) element of the string
print(a[-1]) #access the -1th (last) element of the string

print("--slicing")
#a[start:end]
#a[start:]
#a[:end]
#a[:]
print(a[:4]) #string up until the fifth element of the array
print(a[4:]) #string after and including the fifth element of the array

print(a[2:4])
print(a[0:9])


print("--Lists")
a = [7, 6, 5, 4, 3, 2, 1] #list containing 3 integer elements

b = [3, 2, 1, "hello world"] #lists can contain elements different types

print(a)
print(b)

print(len(a))

print(a[0])
print(a[-1])

print(a[1:]) #from this position print
print(a[:1]) #until this position print

a.append(0) #insert 0 at the end of the list

print(a)

a.insert(0, 4) #insert 4 at element 0 (start of the list)

print(a)

a.remove(4) #this operation only removes the first item in the list equal to 4

print(a)

a.pop() #removes the last item of the list

print(a)

a.pop(0) #removes the 0th item of the list

print(a)

a.sort()

print(a)

a.reverse()

print(a)