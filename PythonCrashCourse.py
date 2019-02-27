#int 
print("--ints")
a = 2
print(a, type(a))
a += 1 #equivalent to a = a + 1 (python does not have a ++ operator)
print(a, type(a))
a *= 2 #equivalent to a = a * 2
print(a, type(a))

#float
print("\n--floats")
b = 1.
print(b, type(b))
b = 1.5
print(b, type(b))

#Booleans
print("\n--booleans")
a = True
b = False

print(type(a))
print(a and b) #note that all logical operators (other than xor) are words and not symbols
print(a or b) 
print(not a)
print(a != b)

#if else Statements
print("\n--if else")
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

###########################################
print("\n--string concatination")
a = "compupter"
b = "1234567"
a += b #string concatenation

print(a)

print(len(a)) #length
print(a, type(a))
print(a[0]) #access the 0th (first) element of the string
print(a[-1]) #access the -1th (last) element of the string
##########################################
print("\n--slicing")
#a[start:end]
#a[start:]
#a[:end]
#a[:]
print(a[:4]) #string up until the fifth element of the array
print(a[4:]) #string after and including the fifth element of the array

print(a[2:4])
print(a[0:9])

#################################
print("\n--Lists")
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
#####################################
print("\n--Iterating")

for element in a: #lists are iterable -- for each element in a
    print(element)

for sameElement in a: #lists are iterable -- for each element in a
    print(sameElement)
#
for i in range(len(a)): #standard for loop -- range(len(a)) creates a sequence of numbers between 0 and the length of a
    print("Index",i,"Element at index",a[i])
#
i = 0
while i < len(a): #standard while loop
    print(a[i])
    i += 1
#
b = [x * 2 for x in a]

print(b)

#equivalent to

c = []

for x in a:
    c.append(x * 2)
    
print(c)
#######################################
print("\n--Aliasing and copying") #pointer to an object 

a = [1, 2, 3]

c = a #c is now an ALIAS to a (not a new list)

a.append(4) #add to original list

print(c) 

d = a[:] #copying through slicing entire list

import copy

e = copy.copy(a) #creates a shallow copy of a -- creates a NEW list and inserts REFERENCES to objects found in original list

f = copy.deepcopy(a) #creates a deep copy of a -- creates a NEW list and recursively adds COPIES of objects found in original list

print("before making changes to a")
print("is a",a)
print("is d",d)
print("is e",e)
print("is f",f)

print("after making changes to a")
a.append(5) #add to original list
print("is a",a)
print("is d",d)
print("is e",e)
print("is f",f)

#################################
print("\n--Dictionaries")

g = dict(one = 1, two = 2, three = 3)

print(g)

h = {'one':5, 'two':3, 'three':8} 

print(h)

j = dict([('two', 2), ('one', 1), ('three', 3)])

print(j)

k = dict({'three': 3, 'one': 1, 'two': 2})

print(k)
##########################
print("\n--Sets")

grades = ['76', '85', '92', '76']

grades_set = set(grades)

print(grades_set) #duplicates have been removed

l = set([1, 2, 3, 4])
m = set([3, 4, 5, 6])

print(l - m) #difference
print(l | m) #union
print(l & m) #intersection
print(l ^ m) #symm difference

print("\n--functions")
#functions, seems doesn't need brackets
a = [1, 2, 3, 4]
b = 3
for element in a:
    if element == b:
        print(True) 
    else:
        print(False)

print("list_contains")
#functions
def list_contains(input_list, element_to_check):
    for element in input_list:
        if element == element_to_check:
            return True
    return False        

a = [10, 11, 12, 13]
print(list_contains(a, 10))
print(list_contains(a, 20))

print("\n--Classes")

class Employee:
    def __init__(self, name, salary): #this method is known as a constructor and is called each time we create a new Employee object
        self.name = name #self refers to the current object -- here we are setting the object's name
        self.salary = salary
        
    def give_pay_rise(self, amount):
        self.salary += amount
        
    def print_employee_data(self):
        print("Employee name:",self.name,"\tEmployee's salary",self.salary)


doug = Employee("Doug", 50000) #create a new Employee object with name "Doug" and salary 50000

doug.print_employee_data()

sarah = Employee("Sarah", 65000) 

sarah.print_employee_data()

sarah.give_pay_rise(234)

sarah.print_employee_data()

#give doug a pay rise and then display his data again
doug.give_pay_rise(10000)
doug.print_employee_data()

print("\n--Doggo")

class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.trick = trick

    def print_dog_data(self):
        print("Doggo name:",self.name,"\tDoggos tricks",self.trick)
        
dog = Dog("Buddy")
dog.add_trick("roll over")

dog2 = Dog("Lucy")
dog2.add_trick("shake hands")

dog2.print_dog_data()

