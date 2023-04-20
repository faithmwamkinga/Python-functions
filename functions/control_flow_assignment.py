# Write a function that uses while, if and continue statements
#  to print all the even numbers between 0 and 50.
def even_numbers():
    x=1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x) 

# Write a function that takes an integer argument and
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.

def prime_numbers(my_intergers):
        if my_intergers<=1:
            print("Not a prime")
        for i in range(2,my_intergers):
            if my_intergers%2==0:
                print("not Prime")
                break
        else:
            print("prime")        
      
   
# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.
def sum_of_even_no():
    total=0
    for y in my_list:
        if y%2==0:
            total+=y
    print(total)
my_list=[1,2,3,4,5,6,7,8,9,10]

#Write a function that takes any two integers as input, and prints the sum of all the 
# numbers between the two integers (inclusive) that are divisible by 3.
def two_integers(numeral1,numeral2):
    my_total=0
    for i in range(numeral1,numeral2):
        if i%3==0:
            my_total+=i
    print(my_total)





