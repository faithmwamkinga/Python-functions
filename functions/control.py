def even_numbers():
    x = range(10)
    for i in x:
        if i%2==0:
            print(i)
    
def odd_numbers():
    y = range(20)
    for i in y:
        if i %2==1:
            print(i)

def divisible_by_five():
    x = range(50)
    for i in x:
        if i %5==0:
            print(f"{i} is divisible by five")
        else :
            print(f"{i} is not divisible by five ")

def divisible_by_many_no():
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by five")
        elif i%7==0:
            print(f"{i} is divisible by 7")
        elif i%9==0:
            print(f"{i} is divisible by 9")
        else:
         print(f"{i} is not divisible by 5,7,or 9")

# combining if statement with logical operators
def divisible_odd_or_even():
    x = range(20)
    for i in x:
        if i%2==0 & i%3==0:
            print(f"{i} is divisible by 2 and 3")
        elif i %2==0 | i%3==0:
            print(f"{i} is divisible by either 2 or 3")
        else :
            print(f"{i} is not divisible by both 2 and 3") 

def while_loop():
    x=1
    while x<10:
        print("Hello")
        x+=1

def break_statement():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break

def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x%3==0:
            continue
        print(x)


