print("my name is anuja")    #print in different line 
print("i am a cse student")

print("my name is anuja.", "i am a cse student.")  #seprated by commas print in same line 


print(45)   #can also print no.
print(10+20) #can also do operations
print(20-10)


#variables and how to use them
name="anuja"
age=20
price=24.87       #here the right side value gets store to the left side

print(name)
print(age)

print("my name is:",name)
print("my age is :",age)


#data types identifications
print(type(name))
print(type(age))
print(type(price))   

#string data types
print("i am anuja an aspiring aiml engineer")
print('i am anuja an aspiring aiml engineer')
print('''i am anuja an aspiring aiml engineer''')


#print sum
a=22
b=50
sum=a+b
print(sum)

diff=a-b
print(diff)


#COMMENTS
# use for single line comment

""" 
multiline 
comment
"""
#shortcut of comment line is = ctrl + /

#arithmetic operators
a=2
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)    #remainder
print(a**b)   #a^b


#assignment operators
num=10
num += 10 #is same as num=num+10
print("num:",num)

num -= 10
print("num:",num)

num *= 10
print("num:",num)

num /= 10
print("num:",num)

#logical operators

print(not False) #will print True
print(not True) #will print False

a=30
b=10
print(not(a<b))

val1=True
val2=False
print("and operator:",val1 and val2)
print("or operator:",val1 or val2)

#type conversion
a=2              #it will convert int into float value auto.
b=2.11
print(a+b)

# a=("2")           #it will give an error as commas are used for string
# b=2.11
# print(a+b)

a=int("2")          #it will convert the str into int as guided 
b=3.32
print(a+b)

#INPUT IN PYTHON

input("enter your name:")       #input passed to the program 

#input passed with a variable
name=input("enter your name:")   
print("Welcome ",name)

name=input("enter name;")
age=input("enter age:")
marks=input("enter marks")

print("welcome",name)
print("age=",age)
print("marks=",marks)


#PRINT TO INPUT 2 NO AND PRINT THEIR SUM

first=int(input("enter first no"))
second=int(input("enter second no"))
print("sum=", first+second)


#input side of sq and print area
a=float(input("enter side"))
print("area of square:", a*a)  


#WAP TO INPUT 2 FLOATING POINT NO AND PRINT THEIR AVG

a=float(input("enter no"))
b=float(input("enter no"))
print("avg:", (a+b)/2)