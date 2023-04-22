# principal=int(input("What is the Principal: "))
# Rate_of_interest=int(input("What's The Rate of Interest: "))
# Time_span=int(input("What is the time span(in years): "))

# Simple_Interest=(principal*Rate_of_interest*Time_span)/100

# print(principal,"is the Principal",",",Rate_of_interest,"Is the Rate of Interest",",",Time_span,"Is the Time Span in years")
# print("The Simple Interest is",Simple_Interest)

# a=23
# b=12

# # a=b
# # b=a
# # print(a)
# # print(b)
# temp=a
# a=b
# b=temp

# print(a)
# print(b)


# ---------------------------------------------------------------------------------------------

# Python program to check
# if a string is palindrome
# or not
 
# FIRST METHOD to Check whether given string is palindrome or not.
# name=input("Enter the word: ")
# name = name.lower()
# reversed_word = ""
# for i in name:
#     reversed_word = i + reversed_word

# print("Your Reversed Word is",reversed_word)
# print("Your Original word was",name)
    
# if (name == reversed_word):
#     print("Yes,The given string is a palindrome!")
# else:
#     print("No,The given string isn't a palindrome!")


# SECOND METHOD FOR PALINDROME CHECKING(WORD)
# string=input(("Enter a string:")).lower()

# if(string==string[::-1]):
#       print("The Word",string[::-1]," is a palindrome")
# else:
#       print("The Word",string[::-1],"Not a palindrome")

# ------------------------------------------------------------------------------------------

# name="Alexander the Great!"
# print(name[0:])
# print(len(name))
# print(name[0:15:3])
# print(name[:])
# print(name[6])

# print(int(3.14))
# print(int(3+6j))  #can't convert complex to int
# print(int(True))
# print(int(False))
# print(int("benson"))


# temperature=int(input("Enter the Temperature: "))
# print("The Temeperature is",temperature)

# if (temperature>20):
#     print("It is Hot")
# elif(temperature==20):
#     print("It's Pleasant")
# else:
#     print("It's Cool")


# list=["Sarah",12,"Rebecca",9,"Fede",18]
# print(list)
# print(list[3])
# list.append("Qwen")
# list.append(17)
# list.append("Spiderman")
# list.append(28)
# list.pop(0)
# list.remove("Fede")

# print(list)


# list1=[3,6,9,17,15,12,18,20,19,28]
# list1[0]=100
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)
# print(list1[2])


# a=(10,12,16,19,22,14,18,30)
# print(a)
# b=((a)+(101,102))
# print(b)


# mydict={"Benson":"Brave","Qwen":"Spiderman","Argentina":"World Cup","India":0.1}
# print(mydict)

# #check whether given letter is vowel
# letter=input("Enter your letter: ")

# list1=["a","e","i","o","u"]

# if letter in list1:
#     print("The letter",letter,"is a Vowel!")
# else:
#     print("The Letter",letter,"is not a Vowel,But a Consonant!")

#ASCII Code
# letter=input("Enter your letter: ")
# print("The ASCII value of",letter,"is",ord(letter))

#Fibonacci Sequence

# num=int(input("Enter the Number: "))

# i=0
# first_value=0
# second_value=1

# while(i<num):
#     if(i<=1):
#         Next=i
#     else:
#         Next=first_value+second_value
    #     first_value=second_value
    #     second_value=Next
    # print(Next)
    # i=i+1

# for i in range(11):
#     print(i)


# Items in a List
# cars=["Buggati","Ferrari","Benz","Audi","Lambhorghini","Jaguar","Mustang"]
# for i in cars:
#     print(i)



# Table

# num=int(input("Enter the Table Number: "))

# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# For loop ("Repeating a Sentence")

# for i in range(11,1,-1):
#     print("Benson"*i)



# Table using While loop
# num=int(input("Enter the Number: "))

# i=0
# while (i<11):
#     i+=1
#     print(num,"x",i,"=",num*i)



# Week Day using While Loop
# i=0
# while (i<5):
#     i+=1
#     print("Week",i)
#     j=0
#     while (j<7):
#         j+=1
#         print("Day",j)

#         print(i,j)

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")



# Function And Calling A Function.

# def login():
#     while True:
#         username=input("Username: ")
#         password=input("password: ")
#         if username==password:
#             print("Successfull!")
#             break
#         else:
#             print("failed")

# login()




# Passing an Argument in a Function.

# def info(username,password):
#     print("Username: ",username)
#     print("Password: ",password)

# info("Sarah","Sophia")

# ---------------------------------------------------------------------------------------------

# function passing an argument

# def func(name):

#     for i in name:

#         print(i,end="")
# func("benson")



# function passing an argument

# def func(name):
#     j=0
#     for i in name:
#         if i=='d':
#             print("The character present at index number",j,"value is : ",name)
#             break
#         j=j+1

# name=input("enter name: ")
# func(name)



# ADDING USING FUNCTION(WITHOUT PARAMETER)

# def add():    
#     x=10
#     y=20
#     c=x+y
#     print(c)

# add()



# FUNCTION BY PASSING ARGUMENTS

# def add(x,y):
#     c=x+y
#     print("The Addition of X and Y is",c)

# add(7,9)



# Sample Function

# def msg(name="Benson"):  #Here we are passing a Default Argument
#     print("Hello,Good Morning!!",name)

# msg("Alexander")  #We can also pass an argument here,if not passed here above Default argument will be taken.



# ----------------------------------------------------------------------------------------------

# Return in Function

# def add(y):
#     x=10
#     c=x+y
#     return c

# sum=add(33) 
# print("The Sum is",sum)



# ---------------------------------------------------------------------------------------------
# Function for Login

# def login():
#     count=1
#     while count<=3:
        
#         while True:

#             username=input("Enter the Username: ")
#             password=input("Enter the Password: ")

#         if username==password:
#             print("Login Succesfull!!!")
#             break
#         else:
#             print("Login Unsuccesfull!!")
#             print("Try Again!!!")
 
# login()


# ----------------------------------------------------------------------------------------------
# Login Function
# With Attemps
# Credentials


# print("Enter Your Credentials")
# count=1
# while count <= 3:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if password==username:
#         print("************************************")
#         print("*                                  *")
#         print("*                                  *")
#         print("*                                  *")
#         print("*             WELCOME!!!           *")
#         print("*                                  *")
#         print("*       LOGGEDIN SUCCESFULLY!!!    *")
#         print("*                                  *")
#         print("*                                  *")
#         print("*                                  *")
#         print("************************************")
        
#         break
#     else:
#         print("Wrong Credentials! Try again!!!")
#         count += 1
#         if count==4:
#             print("Too Many Attempts!Try Soemtime Later!!!")
#             break
        
#         print("This Is Your Attempt",count)
#         if count==4:
#             print("Too Many Attempts!Try Sometime Later!!")




# ----------------------------------------------------------------------------------------------

# HOMEWORK QUESTIONS

# 1.)Python program to add 2 numbers
# 2.)Python Program to find maximum of 2 numbers
# 3.)python program for simple interest
# 4.)python program for compound interest
# 5.)python program to find area of circle



# HOMEWORK QUESTION 01---------->>>(|||Python program to add 2 numbers.|||)

# def add(x,y):
#     z=x+y
#     print("The Sum of Numbers",x,"and",y,"is",z)

# add(10,22)

# HOMEWORK QUESTION 02------->(|||Python Program to find maximum of 2 numbers.|||)

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))

# if num1>num2:
#     print("The number",num1,"is greater!!")
# else:
#     print("The number",num2,"is greater!!!")

# HOMEWORK QUESTION 03-------->(|||Python program for simple interest|||)

# principal=int(input("What is the Principal: "))
# Rate_of_interest=int(input("What's The Rate of Interest: "))
# Time_span=int(input("What is the time span(in years): "))

# Simple_Interest=(principal*Rate_of_interest*Time_span)/100

# print(principal,"is the Principal",",",Rate_of_interest,"Is the Rate of Interest",",",Time_span,"Is the Time Span in years")
# print("The Simple Interest is ₹",Simple_Interest)

# HOMEWORK QUESTION 04-------->(|||python program for compound interest|||)

# Where,
# P = principal
# r = rate of interest
# n = time (in years)

# p = int(input("principal: "))
# r = int(input("rate of interest: "))
# n = int(input("time(in years): "))

# amount=p*(1+r/100)**n
# ci=amount-p

# print("The Compound Interest is ₹",ci)


# HOMEWORK QUESTION 05----------->(|||python program to find area of circle|||)

# import math as m

# radius=int(input("Enter the Radius of Circle: "))

# Area=m.pi*(radius)**2

# print("Area of Circle is",Area,"sq.units")



# ------------------------------------------------------------------------------------------------

# IMPORT IN PYTHON------------------------------------------------------------------------------

# import math as m

# z=m.pi

# # print("The Value of Pi is",z)
# s=int(m.sqrt(25))
# print("The Squareroot is",s,"and The Value of Pi",z)

# import math

# s=math.ceil(10.2)
# f=math.floor(10.9)
# a=math.fabs(-10.7)

# print("The Ceil Value is",s)
# print("The Floor Value is",f)
# print("The Absolute Value is",a)


# -----------------------------------------------------------------------------------------------

# import random as r   #This is how we import a module to access it's function

# list1=["A","B","C","D","E"]
# for i in range(0,3):  #Range mentions the number of Random Letters you want to generate.

#     print("Random Alphabet is",r.choice(list1))   #Choice is used to generate random alphabet/string.
# r.choices gives the list value like    ['B] or ['C'] in this manner
# r.choice gives the particular aplphabet like  A or E or C

# ----------------------------------------------------------------------------------------------
# for i in range(0,3):    #Import random module to access random functions.
#     print("The Random Integer(s) is/are-->",r.randint(1,12))  #randint is used to generate random integers


# for i in range(0,3):
#     print("Random Float Value(s) is/are--->",r.uniform(1,20))#uniform is used to generate random float values.

#  -----------------------------------------------------------------------------------------------   


# THE FUNCTION BELOW IS CALLED IN THE FILE   '''MODULE2'''
# def hello():
#     print("Hello Benson!!!")
#     print("How Are You?")  #THIS FUNCTION SHOULDN'T BE CALLED HERE,IF CALLED IT WILL PRODUCE THE OUTPUT IN THE FILE '''MODULE2'''  2 TIMES!!!
# hello()

# -----------------------------------------------------------------------------------------------

# Message Function

# def welcome():
#     print("Welcome Hello!")

# welcome()

# ==============================================================================================

# num=int(input("Enter your Number: "))
# list1=[0,2,4,6,8]
# # list2=[3,5,7,9]

# a=num[-1]
# print(a)

# if a in list1:
#     print("The Number",num,"is EVEN!!")
# else:
#     print("The Number",num,"is ODD!!")

# ===================================================================================================


# HOMEWORK QUESTIONS 

# 1.)Python program to find Number is prime or not
# 2.)Python program to find number is even or not
# 3.)Python program to check whether given character is vowel or not
# 4.)Python program for Fibonacci sequence
# 5.)Python program to check whether given number is palindrome or not

# HOMEWORK QUESTION 01---->(Python program to find Number is prime or not)
# num=int(input("Enter the Number: "))
# prime=True

# for i in range(2,num):
#     if num%i==0:
#         prime=False
#         break
# if num==1:
#     print("Neither Prime nor Composite")
# elif prime:
#     print("Prime")
# else:
#     print("Not Prime")





# HOMEWORK QUESTION 02----->(Python program to find number is even or not)
# num=int(input("Enter the number: "))

# if (num%2==0):
#     print("The Number",num,"is EVEN!")
# else:
#     print("The Number",num," is ODD!")





# HOMEWORK QUESTION 03--->(Python program to check whether given character is vowel or not)
#check whether given letter is vowel
# letter=input("Enter your letter: ")
# z=letter.lower()
# list1=["a","e","i","o","u"]

# if z in list1:
#     print("The letter",letter,"is a Vowel!")
# else:
#     print("The Letter",letter,"is not a Vowel,But a Consonant!")



# HOMEWORK QUESTION 04---->(Python program for Fibonacci sequence)

# num=int(input("Enter the Number: "))

# i=0
# first_value=0
# second_value=1

# while(i<num):
#     if(i<=1):
#         Next=i
#     else:
#         Next=first_value+second_value
#         first_value=second_value
#         second_value=Next
#     print(Next)
#     i=i+1


# HOMEWORK QUESTION 05--->(Python program to check whether given number is palindrome or not)
# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number",temp,"is a Palindrome!!")
# else:
#     print("The Number",temp,"not a palindrome!")




# FILE HANDLING
# f=open('sample09.txt','r')
# data=f.read()
# print(data)
# # f.close()

# f=open('sample09.txt')
# data=f.read()  #Returns all the contents in the file
# data=f.readlines()  #Returns the content in the file in List Format!
# data=f.readlines()[0]  #Gives the particular line (We can access just like the way we access a list)
# data=f.readline()  #Returns the first line
# data=f.readline()  #Returns the Second line
# data=f.readline()  #Returns the Third line
# data=f.readline()  #Returns the Fourth line

# print(data)

# -------------------------------------------------------------------------------------------------


# Exception Handling
# try:
#     print(5/0)

# except ZeroDivisionError as msg:
#     print("The error is",msg)


# Exception Handling
# try:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print(a/b)
# except (ZeroDivisionError,ValueError) as msg:  #This gives the error description.
#     print("Enter only Integer value!")
#     print("The error is",msg)

# finally:   #finally is used to print a statement at the end regardless of try and except.
#     print("I will always be printed no matter what")
# print("I will always be printed,no matter what!")

# Exception Handling
# bank_bal=8000
# if bank_bal<1000:
#     raise Exception("Your Account is below the accessing limit!")
# else:
#     print("Your Account has withdrawal!")

# HOMEWORK QUESTIONS 
# 1.)Python Program to find Area of Triangle.
# 2.)Python Program to Swap 2 Variables.
# 3.)Pyhton Program to check leap year.
# 4.)Python Program Simple Calculator.
# 5.)Python Program Temperature Celcius to Farenheit.



# HOMEWORK QUESTION 01--->(Python Program to find Area of Triangle.)
# try:
#     height=int(input("Enter the Height of the Triangle: "))
#     base=int(input("Enter the Base of the Triangle: "))

#     area_of_triangle=(0.5)*base*height

#     print("The Area of Triangle is",area_of_triangle,"sq.units")
# except (ValueError) as msg:
#     print("This is the error---->",msg)

# finally:
#     print("Hello!,I'll be there always!!!")



# HOMEWORK QUESTION 02--->(Python Program to Swap 2 Variables.)
# a="Benson"
# b="Real Madrid"
# print("The Values BEFORE Swapping were a-->",a,"and b-->",b)
# a,b=b,a

# print("The Values AFTER Swapping are a-->",a,"and b-->",b)
# print("See how the Variables got swapped!")



# HOMEWORK QUESTION 03--->(Pyhton Program to check leap year.)
# year=int(input("Enter the Year: "))
# if year not in range(0,9999):
#     print("Enter Year between 0 to 9999")
# elif year%4==0:
#     print("The Year",year,"is a Leap Year!!!")
# else:
#     print("The Year",year,"isn't a Leap Year,but a Common Year!!!")



# HOMEWORK QUESTION 04--->(Python Program Simple Calculator.)
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# def Calculator():
#     num1=int(input("Enter the first number: "))
#     num2=int(input("Enter the second number: "))
#     print("The sum of num1 and num2 is",num1+num2)
#     print("The difference of num1 and num2 is",num1-num2)
#     print("The product of num1 and num2 is",num1*num2)
#     print("The division of num1 and num2 is",num1/num2)
#     print("All operations are performed!!!")

# Calculator()


# HOMEWORK QUESTION 05--->(Python Program Temperature Celcius to Farenheit.)    
# try:
#     choice=float(input("ENTER YOUR CHOICE \n To Convert from Celcius to Farenheit(Press 1) OR To Convert from Farrenheit to Celcius(Press 2): "))
#     if choice==1:
#         temp=float(input("Enter the temperature(In Celcius): "))
#         farenheit=(temp*1.8)+32
#         print(temp,"°C in Farenheit is",farenheit,"°F")
#     elif choice==2:
#         temp=float(input("Enter the temperatute(in Farenheit): "))
#         celcius=(temp-32)*0.5556
#         print(temp,"°F in Celcius is",celcius,"°C")
#     else:
#         print("Enter a Valid Input!! TRY AGAIN!!")
# except (ValueError) as msg:
#     print("This's the error--->",msg)
#     print("Enter a Valid Input!!TRY AGIN!!")




