
print('i have placed in ksolves(Indore)')
print(5)
print('bye')
print("bye2")
print(12+34)
print(5*2)
name = 'tarun namdev'
age = 20
passed = True
p = 'adk3323'


# local variable and Global vaiable

g1 = "i am global variable"
def foods():
    vegetable = "tomato"
    fruit = "apple"
    print(vegetable, "is a local variable")
    print(fruit, "is a local variable")
    print(g1)

foods()


# List
list1 = [1,2,3,4,"mango", "apple", ["red", "green"]]
print(list1)


# Tuple
tuple1 = ("mango", "apple", ("lion", "bhalu"))
print(tuple1)


# range
sequence1 = range(10+1)
for i in sequence1:
    print(i)


# Dictionary
dict1 = {"name":"Tarun", "age":23, "canVote":True}
print(dict1)


# Set
set1 = {3,1,2,4}
print(set1)
print(type(set1))


#Data-Types
a = 12
b = 0
c = 7.32
d = 2.4E4
e = 2 + 4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#Data-Convertion
a = 5.2
b = int(a)
print(a)
print(b)

a1 = 10
b1 = float(a1)
print(a1)
print(b1)

a2 = 24
b2 = complex(a2)
print(a2)
print(b)



#Type-Casting
str1 = "12"
str2 = "3.233"
print(type(str1))
print(type(str2))

print(int(str1))
print(float(str2))
print(type(int(str1)))


#Pytong-Booleans
x = 12
if(x>10):
    print("x is greater than 10")
else:
    print("x is lesser")

name = "tarun"
print(name == "tarun")
print(bool("tarun"))



#Strings
name = 'tarun'
print('my name is',name)
print("he said, \"I want to eat apple.\"")

note = '''
This is Tarun Namdev.
I am 23 years Old.
and i am doing my best.
'''
print(note)

#length of string
name = 'tarun namdev'
print(len(name))
print(name[0])

#loop throuth a String
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabets:
    print(i)


#string methods
name = 'tarun namdev'
print(name.upper())
print(name.lower())
print(name.strip)
print(name.split())
print(name.replace('tarun namdev','harry'))
print(name)
print(name.capitalize())
print(name.center(50))
print(name.center(50,"*"))
print(name.count('n'))
print(name.endswith('dev'))
print(name.find('na'))
print(name.title())


#Format Strings
name = 'Hero'
age = 18
print(f"my name is {name} and my age is {age}")

  #concatination
str4 = 'captain'
str5 = 'america'
str6 = str4 + " " +str5
print(str6)


#Escape Characters

str1 = 'tarun\'s company'
print(str1)
str = 'another\nline'
print(str)
str = 'another\t\t\t\t\tTab'
print(str)

str = 'apple\\banana'
print(str)


#List
list1 = [1,2,3,4,5]
list2 = ["apple","banana","cherry"]
print(list1)
print(list2)

list3 = ["Red",12, 13, 17.55, 'orange']
print(list3)
 
 #list indexing
list1 = ["red", 'green', 'blue']
print(list1[0])
print(list1[1])
print(list2[2])

 #negative indexing
print(list1[-1])
print(list1[-2])

 #check for item
if 'red' in list1:
    print("yeah it is present inside.")
else:
    print("not present")


 #append():
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

 #insert():
names = ["tarun", "neha", "gupta"]
names.insert(1,"namdev")
print(names)

 #extend():
names = ['tarun','neha']
casts = ['namdev','gupta']
names.extend(casts)
print(names)

 #concatenate two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)

 #pop():
colors = ["voilet", "indigo", "blue", "green"]
colors.pop()
print(colors)

colors.pop(2)
print(colors)
colors.remove('voilet')
print(colors)
# del(colors)
print(colors)
colors.clear()
print(colors)


 #sort():
num = [1,2,3,92,1,2,987,12,13,322,2]
num.sort()
print(num)


 #reverse():
 #acending
num = [1,2,3,92,1,2,987,12,13,322,2]
num.reverse()
print(num)
 #decending
num.sort(reverse=True)
print(num)

 #copy():
names = ['tarun','neha']
names2 = names.copy()
print(names)
print(names2)
names2.append('gupta')
print(names2)




 #Python Tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,2,3,4,5)
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))

 #Manipulating Tuples - 
 # Tuple are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.'''
 
tuple1 = ("apple", "banana", "cherry")
temp = list(tuple1)
temp.append("orange")
tuple1 = tuple(temp)
print(tuple1)
print(type(tuple1))



countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

#Concanate tuple
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)



 #Python Sets
info = {"tarun", 12,2,34,5}
print(info)
print(type(info))

for i in info:
 print(i)

cities = {"delhi", "mumbai", "bangalore", "chennai"}

cities.add("Lucknow")
print(cities)

cities.remove("delhi")
print(cities)

#other methods - pop, del, clear

if "mumbai" in cities:
    print("present")
else:
    print("not present")

#union() and update(): - union return the new set whereas update add in it.

friend1 = {"tarun", "neha", "gupta"}
friend2 = {"vikas", "tanvi", "sharma"}
friend3  = friend1.union(friend2)
print(friend3)

friend1 = {"tarun", "neha", "gupta"}
friend2 = {"vikas", "tanvi", "sharma"}
friend1.update(friend2)
print(friend1)


#Intersection and intersection_update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)



#Dictionary
info = {'name':'Tarun', 'age':23,
'eligible':tuple}
print(info)
print(type(info))
 #accessing dictionay item
print(info['name'])
print(info.get('name'))

 #accessing multiple values
print(info.values())

 #accesing keys
print(info.keys())
 #accessing key-value pairs
print(info.items())


#copy Dictionaries
info = {'name':'tarun', 'age':23}
newinfo = info.copy()
print(newinfo)

#if Statement
applePrice = 200
budget = 200
if(applePrice <= budget):
    print("i can buy")

#if-else
age = 18
if(age>=18):
    print("18years old")
else:
    print("not 18 years old")

#if-elif-else

if(age < 0):
    print("number is negative")
elif(age == 0):
    print("number is zero")
else:
    print("numbet is positive")


#for-loop
characters = 'abcdefghijklmnopqrstuvwxyz'
for i in characters:
    print(i)

colors = ['red', 'green', 'blue']
for i in colors:
    print(i)


for k in range(12):
    print(k+1)

for k in range(5, 10):
    print(k+1)


#while-loop

#pass
def sayHello():
    pass
#continue
for i in range(10):
    if i == 5:
        continue
    print(i)

#break
for i in range(20):
    if i==5:
        break
    print(i)



#functions
def sayHello(fname, lname):
    print("hello", fname, lname)
sayHello('tarun', 'namdev')


def add(a,b):
    return a+b
print(add(2,3))

#default arguments

def nameCall(fname, mname="kumar", lname="namdef"):
    print('hello', fname, mname, lname)

nameCall('tarun')


#return statement
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))



def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))
    
num = 5
print("Factorial of ", num , " is ", factorial(num))


#Modules
import math
print(math.sqrt(25))
print(int(math.sqrt(25)))
print(math.sin(30))
print(math.tan(30))
print(math.tan(90))

#import module
#import math as m
# from module import add, sub
#from module import *

#dir() function
import math
list1 = dir(math)
print(list1)



#Creating a Class:

class Details:
    name = "Tarun"
    age = 23
    def sayHello(self):
     print("hello")
obj1 = Details()
print(obj1.name)
print(obj1.age)
obj1.sayHello()


#Self Method
class Details:
    name = "Simran"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()


#Coonstuctors

class Details:
    def __init__(self, animal,group):
        self.animal = animal
        self.group = group

obj1 = Details("Lion", "Mammal")
print(obj1.animal)
print(obj1.group)



#Python try...except
try:
    num = int(input("enter an integer"))
except:
    print("invalid input")


#else block
try:
    num = int(input("enter an integer"))
except:
    print("invalid input")
else:
    print("Integer Accecpeted")

#try...except...finally
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")




#Date & Time
import time
print(time.time())

#These numbers are nothing but the number of ticks since the start of January 1, 1970 also called as epoch.

#Now, one might ask what are ticks?

# Ticks are floating point numbers measured in units of seconds for time interval.



import time
print(time.ctime()) #human readable format

time.sleep(10) #it will delay execution 10 seconds

print(time.localtime())



#Calaender
import calendar
print(calendar.month(2025, 1))

'''
This is a multiline
comment.
'''


#File Handling
file = open("file.txt")
print(file.read())


 #write on to a file
file = open('Text.txt', 'w')
file.write("this is new text")
file.close()

 #read a file
file = open('text.txt', 'r')
print(file.read())
file.close()

    #append to a file
file = open('text.txt', 'a')
file.write("this is appended text")
file.close()



#Decorators
 #regular function -
def square(x):
    return x*x
square(5)

#lambda function
square_lambda = lambda x: x*x
print(square_lambda(5))

#lamda function with multiple arguments
add = lambda a,b: a+b
print(add(2,5))

#Using lamda insider another function
def multipleFunc(n):
    return lambda a: a*n
double = multipleFunc(2)
print(double(4))


#Decorators

