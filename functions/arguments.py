def year_of_birth(name,age):
    year = 2023-age
    print (f"Hello{name} your were born in {year_of_birth}")
    
def my_country(country = "Kenya"):
    country = "Rwanda"
    print (f"Hello you are from{country}")

# Write a function that accepts any no of arguments
def hello (*names):
    for name in names:
         print(f"Hello{name}")

def sum (*nums):
    sum = 0
    for num in nums:
        sum+=num
        return sum
def multiply_many(**kwargs):
    answer = 1
    for num in kwargs.values():
        answer*=num
        return answer 

def  concatenate_args (*cities): 
    strings= ""
    for city in cities  :
        strings+=city
    return strings

def  concatenate_kwargs(**kwargs):
    arguments =""
    for word in kwargs.values():
        arguments+=word
    return arguments
        
       

   


