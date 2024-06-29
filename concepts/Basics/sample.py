#slicing is a create a substring to extract elements

import random


web="https://google.com"
web1="https://ranjithkumar.com"

slice=slice(8,-4)

print(web[slice])

print(web1[slice])


#if statement

age=int(input("Enter your age:"))
if age<18 and age>0:
    print(age," age")
elif age<30 or age<35:
    print(age," age spr")
else:
    print(age," is you age")
    
    
#while loop
name=""
while len(name)==0:
    name=input("Enter your name:")
    

#for loop
for i in range(1,10):
    print(i)
    
for i in "Ranjith":
    print(i)
    
#nested loop

rows=int(input("Enter the no. of rows:"))

cloumns=int(input("Enter the no. of cloumn:"))
symbol=input("Enter teh symbol:")

for i in range(rows):
    for j in range(cloumns):
        print(symbol,end="")
    print() 


#list-Used to store multiple items in single variable
#See more in videos or foods. using 

foods=["Apple","bananana"]

print(foods[1])
for x in foods:
    print(x)
    
#2D list
a=["a","b"]
b=["c","d"]
c=[a,b]
print(c[1])
print(c[0][1])


#tuple=collection whiuch are ordered and unchangeable
student=("Bro",25,'a')

print(student.count("Bro"))
print(student)

if "Bro" in student:
    print("Bro is here")
    

#set=collection whiuch is unoreded ,unindexed and no duplicate value
#see more in a.
a={"a","b","c"}
b={"d","e"}
a.update(b)
for x in a:
    print(x)
    

#dictionary
capitals={
    'a':'A',
    'b':'B',
    'c':'C'
}

print(capitals["a"])
print(capitals.values())
print(capitals.keys())
print(capitals.get('d'))#Remove the error 
print(capitals.items())

for key,value in capitals.items():
    print(key," = ",value)

#index operator[]=Give access to a sequence element (str,list,tuple)

name="bro code"
first_name=name[:3].upper()
last_character=name[-1]
print(first_name)
print(last_character)


#function=a block of code executed only when it called

def name(first_name,last_name,age):
    print(first_name+" "+last_name,"age is",age)


name("Ranjith","Kumar",19)


#return statement=function sends a msg return to the caller

def mul(num1,num2):
    return num1*num2

print(mul(2,2))


#2.10 completed

#*args==used for more parameter adding

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return(sum)
print(add(1,2,3,4))


#**kwargs

def join(**kwargs):
    print("Hello "+kwargs['first']+" "+kwargs['last']+" "+kwargs['middle'])
    
join(first="Ranjith",middle="S",last="Kumar")


#str.format
#see more in video 
a="A"
b="B"
print("The {} is the {}".format(a,b))

print("The {1} is the {0}".format(a,b))#Positional argument

n=3.22345
n1=1000
print("The n is {:.2f}".format(n))
print("The n in binary is {:b}".format(n1))

#Random

x=random.randint(1,6)
print(x)

mylist=["a","b","c"]
z=random.choice(mylist)
random.shuffle(mylist)
print(z)
print(mylist)


