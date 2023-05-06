# conditions
def my_names(namesake):
    # name = "Sakina"
    print ({namesake}) 

def multiplication(num1,num2):
    product =num1*num2
    if (product<=1000):
            print( product)
    else:
        print(num1+num2)


def sum_and_multiplication(sum,multiplication):
     return f"The sum of 3, 4 and 5 is{sum} and the product of 4 and 4 is {multiplication}"
print(sum_and_multiplication(3+4+5,4*4))

def sum1_and_multiplication2 (sum1,multiplication2):
     return f"The sum is {sum1} and their product is {multiplication2}"
print(sum1_and_multiplication2(7+6+9+3,3*9*7))

def names(firstname="a",secondname="b"):
     return (f"my name is {firstname} {secondname}")
print(names())
print(names(firstname="Faith"))
print(names(firstname="Faith",secondname="Mwamkinga"))
print(names(secondname="Mwamkinga"))
print(names(secondname="Mwamkinga",firstname="Faith"))

def my_names(*namess):
    final =[name for name in namess]
    print(f"hello{final}")

my_names("Faith","Rose","Glory")

def ournames(*student_names):
     for name in student_names:
          print(name)

ournames("Joune","Juma","Ismail")

# def addition(integers):
     # sum =0
     # for inte in range(0,10):
    #  for inte in range(0,10):
          # total =sum+ inte
        #   return sum
     # print("current number",inte,"previous number",sum,"sum:",total)

def palindrome(word):
     word="noon"
     pali = word[::-1]
     if pali==word:
      print("true")
     else :
      print ("false")

def pally(verb):
    verb = "Civic"
    vocabulary =verb.lower()
    vocabulary1 = vocabulary[::-1]
    if vocabulary == vocabulary1:
        print("true")
    else: 
        print("false") 

# Given two integer numbers return their product only if the product
#  is equal to or lower than 1000, else return their sum. 
def both(a,b):
    if a*b<=1000:
        product=a*b
        print(product) 
    else:
        print(a+b) 

# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

x =[1,2,3,4,5,6,7,8,9,10,11]
def two_numbers(current,previous):
    
    
    for i in range(1,len(x)):
     current=x[i]
     previous=x[i-1]
     summation=current+previous
     print(summation)

# Write a program to accept a string from the user and display 
# characters that are present at an even index number.
def wordy():
    word="Mercy"
#     word=input("Enter a string:")
    even=''
    for i in range(len(word)):
        if i%2==0:
          even+=word[i]
          print(even)


nanny=["Mercy","Faith","Joune","Angel","Rose","Juma","Ismail","Indiana"]
first,second,third,*rest=nanny
print(first)
print(second)
print(third)
print(*rest)


numms=[4,2,3,5,6,9,7,8,10]
numms.sort()
print(numms)

numms.reverse()
print(numms)

numms.sort(reverse=True)
print(numms)

my_list=[*range(10,20)]
print(my_list)

del(my_list[0:3])
print(my_list)

my_list.remove(14)
print(my_list)

koko=[1,2,3,3,5,4,4,5,6,7,8,9]
for numbb in koko:
    if numbb==3:
     print(koko)
# del(koko[3])
# del(koko[5])

# Write a program to create a function that takes two arguments, name and age, and print their value.
def person(name,age):
    print(name,age)
    
    
# Home » Python Exercises » Python Functions Exercise
# Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments
# and print their value.
def mine():
#     mimi="notice"
    mama="bibi"
    print(len(mama))
def picture(*pipi):
    print(pipi)

# Write a program to create function calculation() such tha it can accept two variables and  
#  calculate addition and subtraction. Also, it must return both 
# addition and subtraction in a single return call.
def calculation(number1,number2):
    addition=number1+number2
    subtraction=number1-number2
    return (f"The sum is {addition} and difference is {subtraction}")

# Home » Python Exercises » Python Functions Exercise
    # Your Code

# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(names,salary=9000):
     print(names,salary)

# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def main(a,b):
    
  
    
    def inner(a,b):
     return a+b
    add=inner(a,b)
    return add+5
result=main(5,10)
print (result)

def check(a,b):
    c= a is "aa"
    print(c)
    d=b in "dog"
    print(d)
check("umbrella","g")

#Write a python function that takes one argument as a list a = [2,4,6,8] and 
#remove the second last item from that list and returns the whole list without
#the removed item.
def my_list(lists):
    lists=[2,4,6,8]



#write a python function named divisible_by_seven that using the range function
#and a for loop returns a list containing all the numbers divisible by 7.

def divisible_by_seven():
    empty=[]
    x = range(100,200)
    for i in x:
        if i%7==0:
            empty.append(i)
    return empty
print(divisible_by_seven())

#alternative
def divisible_by_seven1():
    y = range(100,200)
    empty1=[i for i in y if i % 7 ==0]
    return empty1
divisible_by_seven1() 

#using for loop, calculate the average of a list in a range of (55,100)
def averages():
    number_list=range(55,100)
    total1=0
    for i in number_list:
        total1+=i
        averagess=total1/len(number_list)
    return averagess
print(averages())

#Using a for loop print odd numbers from 1 to 10
def prime_numbers():
    t = range(1,11)
    for i in t:
        if i >2:
            return i
        elif i % i==1 and i%1==i:
            return i
 
print(prime_numbers())

#Using a while loop print odd numbers from 1 to 10
# start=2
# while (number<=10):
#     for i in range(2,number):
#         if start%i==1 & start%1==start:
#             start+1
#     # if start>2:
#     #     if start[0]%len(start)==0:
#     #         start+=1
# print(start)
def primes(numby):
    if numby<2:
        return False
    for i in range(2,numby):
            if numby %i==0:
                return False
    return True
numby=0
while numby<=10:
    if primes(numby):
        print(numby)
    numby+=1
# primes(numby)        

#Write a program to check whether a year is a leap year or not.
def years():
    yearss=range(2001,2023)
    for i in yearss:
        if i%4==0:
            print(f"${i} is a leap year")
    else:
        print(f"${i} is not a leap year")
    i+=1
years()

#Write a program to accept the percentage the user and display the grade according to the following criteria
# Marks          Grade
# 90               A 
# 80 and <=90      B
# >=60 and <=80    C
#below 60          D

def display_grade(student):
    
        if student<60:
            print("D")
        elif student>=60<80:
            print("C")
        elif student>80<=90:
            print("B")
        elif student>91:
            print("A")
   
display_grade(90)

#Write a program to use for loop to print the following reverse number pattern
def reverse_number_pattern():
    x=range(1,6)
    y=range(1,6)
    i=1
    n=1
    for i in x:
        if i >=1:
            print(i)
    i-=1
    for n in y:
        if n>=1:
            print(n)
    n-=1
reverse_number_pattern()

# Write a Python function that takes two arguments (a and b) and returns their sum.
# Write a Python function that takes a string as input and returns the string reversed.
# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
# Write a Python function that takes a list of integers as input and returns the highest value in the list.
# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.


def my_summation(f,d):
    if f<=d:
        totality=f+d
    return totality
print(my_summation(10,20))

def addi(b,d):
    a+b
print(addi(10,20))

def my_word(worddy):
    worddy="bishop"
    new_word=worddy[::-1]
    return new_word
print(my_word(wordy))

def list_integers(integerz):
    # integerz=[1,2,3,4,5,6,7,8]
    totals=0
    for i in integerz:
        if i<=8:
            totals+=i
    return totals
print(list_integers([1,2,3,4,5,6,7,8]))

def integers_list(integers):
    sum_of_even=0
    for i in integers:
        if i%2!=0 &i<=10:
            sum_of_even+=i
        return sum_of_even
print(integers_list([10,9,8,7,6,5,4,3,2,1]))


def new_odd_list(ints):
    new=[]
    for i in ints:
        if i%2!=0:
            return i
print(new_odd_list())

# CLASSES
# Identity: Every object must be uniquely identified.
# State: An object has an attribute that represents a state of an object, and it also reflects the 
# property of an object.
# Behavior: An object has methods that represent its behavior.

# For example, If we design a class based on the states and behaviors of a Person, 
# then States can be represented as instance variables and behaviors as class methods.

