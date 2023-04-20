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
     

