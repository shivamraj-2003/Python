"""
name='shivam'
age=21
print(name+'is a boy')
# you can't concatnate string and integer in python
print(name+'is',age)

print('Hi\n How are you')
print(name[0])
#string..
name='shivam'

print(name.lower().islower())
print(len(name))
print(name.index('i'))
print(name.replace('s','m'))


#number
number=78
print(78+22.934)
number1=str(number)
print('number is'+number1)
print(min(1,2,4,6))
print(max(5,8,9,16))

from math import *
print('The square root of number is',sqrt(196))


name=78
print(name)
number=input('Input Your Number: ')
print(number)

sentence=input('Enter your sentence: ')
print('your sentence is: '+sentence)
countries=['united kingdom','ghana','nigeria']
print(countries[2])
print(countries[2][0])
print(countries[0:2])
countries[0]='India'
print(countries)

countries=list(('nigeria',34,False))
countries2=['nigeria',34,False]
print(type(countries))
print(type(countries2))


list1.extend(list2)
print(list1)
list2.append('cherry')
print(len(list2))
list2.insert(2,'mango')
print(list2)
list2.remove('muskan')

list1=[1,2,8,9,3,4]
list2=['shivam','kanak','muskan']
list3=list1.copy()
list1.sort()
list2.pop()
del list2[0]
print(list2)
print(list1)
print(list3)

#Tuples....
three=(1,2,3)
# three[1]=23 doesn't work
print(three[0])
strings=('home','land','earth')
print(strings)
number=tuple((1,"Home",True,3,1))
print(number)

#Functions
def greetings():
    print("Hello Shivam")

greetings()


def greetings(name):
    print("Hello "+name)
def greetings(*names):
    print('Welcome '+names[1])

greetings('Shivam','Muskan','Kanak')

def greetings(name,age):
    print('Welcome'+name+ '.You are '+str(age)+' years old')

name=input('Enter your name: ')
age=input('Enter your age: ')
greetings(name,age)

#return keyword
def my_function(num1,num2):
    return num1+num2
num1=int(input('Enter first number :'))
num2=int(input('Enter 2nd numberm :'))

print(my_function(num1,num2))

#if-else
a=2;
b=3;
if a >b:
     print(str(a)+' is greater than '+str(b))
else:
     print(str(a)+' is not greater than '+str(b))

#Program for the check odd/even number
num=int(input('Write a number: '))
if(num%2==0):
    print("Number is Even")
else:
  print("Number is odd")

#Dictonaries in Python

my_dict={
    'name':"Shivam",
    'nationality':'Indian',
    'age':18,
    'friends':['Peter','Shubham']

}
print(my_dict)
x=print(my_dict['name'])

while loops

i=1
while i<6 or i==6:
    print(i)
    #i=i+1;
    i+=1
#For loops

for letter in 'Hello':
    print(letter)

mylist=['ji','ju','jo']
for values in mylist:
    if values=='ju':
     break
    print(values)
for x in range(3,7):
   print(x)

2D-list

my_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(my_list[0][2])
for lists in my_list:
    for row in lists:
     print(row)
Building a Simple calculator

num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
op=input('Enter operator: ')
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print('Invalid operator')

Try Except...
try:
   x=int(input("input an integer: "))
   print(x)
except:
   print('Value not an integer')

   Reading and writing files in Python

file=open('countries.txt','r')
for lines in file.readlines():
    print(lines)
file.close()

file=open('countries.txt','a')
file.write('\nThis is the new country file')

OOPS in python

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

name=input("Enter your name: ")
age=input('Enter your age: ')
p1=Person(name,age)
print(p1.name,p1.age)
"""
def function():
    print('Hi Shivam!')
