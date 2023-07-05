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
     pali = word[::-1]
     if pali==word:
      print("Yes the word is a palindrome")
     else :
      print ("The word is not a palindrome")
    
print(palindrome("noon"))

def pally(verb):
    vocabulary =verb.lower()
    vocabulary1 = vocabulary[::-1]
    if vocabulary == vocabulary1:
        print("true")
    else: 
        print("false") 
pally("Civic")

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
averages()

#Using a for loop print odd numbers from 55 to 100
def prime_numbers():
    t = range(55,101)
    for i in t:
        if i >54:
            return i
        elif i % i==1 and i%1==i:
            return i
 
print(prime_numbers())
prime_numbers()

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
    d+b
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


def new_odd_list():
    numzz=[12,11,23,45]
    for i in numzz:
        if i%2!=0:
            return i
print(new_odd_list())

# CLASSES
# Identity: Every object must be uniquely identified.
# State: An object has an attribute that represents a state of an object, and it also reflects the 
# property of an object.
# Behavior: An object has methods that represent its behavior.

# # For example, If we design a class based on the states and behaviors of a Person, 
# # then States can be represented as instance variables and behaviors as class methods.


class Ankara:
    def __init__(self,temperature,mood,design,new_design):
        self.mood=mood
        self.temperature=temperature
        self.design=design
        self.new_design=new_design
    def detect_pattern_changes(self):
      moods = ["happy","sad","bored"]
      if self.temperature>30 and self.mood in moods:
            return f"The pattern changes from {self.design} to {self.new_design}"
      elif self.temperature<30 and self.mood in moods:
            return f"The pattern changes from {self.design} to {self.new_design}"
      else:
            return f"The pattern does not change"
person=Ankara(20,"sad","Polka dot","Wavy")
print(person.detect_pattern_changes())
person=Ankara(20,"happy","Polka dot","Wavy")
print(person.detect_pattern_changes())

class AnkaraDesignz:
    def __init__(self,temp,mood):
        self.temp = temp
        self.mood = mood
    def predict_changes(self):
        temps = 37
        if self.mood == "happy":
            if self.temp > temps:
                return "Ankara design changes to polkadots"
            if self.temp <temps:
                return "Ankara design changes to checked boxes"
        if self.mood == "sad":
            if self.temp > temps:
                return "Ankara design changes to straight lines"
            if self.temp <temps:
                return "Ankara design changes to wavy"
        else:
            return "Ankara does not change design"
        
design1 = AnkaraDesignz(37,"happy")
design2 = AnkaraDesignz(7,"sad")
design3 = AnkaraDesignz(40,"happy")
print (design1.predict_changes())
print (design2.predict_changes())
print (design3.predict_changes())

# class Ankaras:
#     def __init__(self,temperature):
#         self.temperature=temperature
#     def detect_pattern_changes(self):
#       moods = ["happy","sad","bored"]
#       if self.temperature>30 and moods:
#             return f"The pattern changes to Polka dot"
#       elif self.temperature<30 and moods:
#             return f"The pattern changes to Wavy"
#       else:
#             return f"The pattern does not change"
# person1=Ankaras(30,"sad")
# print(person1.detect_pattern_changes())

# class Ankarar:
#     def __init__(self,temperature,mood):
#         self.temperature=temperature
#         self.mood=mood
#     def get_design(self):
#         design=""
#         if self.temperature<30 and self.mood=="Happy":
#             design="Design changes to Polka dots"
#         elif self.temperature >30 and self.mood=="Sad":
#             design="pattern changes to straight line"
#         elif self.temperature <30 and self.mood=="Sad":
#             design="pattern changes to wavy line"
#         elif self.temperature >30 and self.mood=="Happy":
#             design="pattern changes to boxes"
#         else:
#             design="Design mantains"
# person2=(20,"Sad")
# print(person2.get_design())

# class Annkara:
#      def __init__(self, temperature, mood):
#         self.temperature = temperature
#         self.mood = mood
#         def get_pattern(self):
#             if self.temperature >= 20 and self.mood >= 5:
#               return "Ankara pattern turns to wavy lines."
#             else:
#              return "Ankara pattern designs turn to polka dots."
#         def set_temperature(self, temperature):
#             self.temperature = temperature
#         def set_mood(self, mood):
#             self.mood = mood
# ankara = Annkara(20, 7)
# print(ankara.get_pattern())
# # ankara=Annkara(15,3)
# print(ankara.get_pattern())

    
class Ankara:
    def __init__(self, temperature, mood):
        self.temperature = temperature
        self.mood = mood
    def get_pattern(self):
        if self.temperature >= 20 and self.mood >= 5:
            return "Ankara pattern turns to wavy lines."
        else:
            return "Ankara pattern designs turn to polka dots."
    def set_temperature(self, temperature):
        self.temperature = temperature
    def set_mood(self, mood):
        self.mood = mood
ankara = Ankara(20, 7)
print(ankara.get_pattern())
ankara=Ankara(15,3)
print(ankara.get_pattern())    


#The Great Migration Forecast: Every year, millions of wildebeest, zebras, and other animals 
#participate in the Great Migration across the Serengeti-Mara ecosystem. As a conservationist, 
#you want to develop a software system that models this migration, predicting the movement of the 
#herds based on weather patterns, river levels, and predator locations. Consider what classes you'll
#need to represent the animals, the environment, and the various factors that influence the migration.// 

#The Great migration
class Migration:
    def __init__(self,weather_pattern,river_level,predator_location):
       self.weather_pattern=weather_pattern
    #def __init__(self,predator_location):
     #  self.weather_pattern=("sunny","rainy")
       self.river_level=river_level
      # self.river_level=("high","medium","low")
       self.predator_location=predator_location
    def predict_movement(self,destined_location):
        if "sunny" in self.weather_pattern and "low" in self.river_level and self.predator_location =="Mara" :
            return f"The herd will move to {destined_location}"
        else:
            return f"The herd will not migrate"

#herd_one=Migration("Serengeti")
herd_one=Migration("sunny","low","Mara")
print(herd_one.predict_movement("Serengeti"))

empty_list =[]
class Possible_Fruit:
    def __init__(self,powers,effect,season,name):
        self.powers=powers
        self.effect=effect
        self.season=season
        self.name=name
    def __repr__(self):
         return f"{self.name} {self.effect} {self.powers} {self.season}"
fruits = Possible_Fruit(powers="changecolor",effect="gives energy",season="wet",name="big baobab")
empty_list.append(fruits)
print(fruits)
print(empty_list)
class Seasons:
    def __init__(self,seasons):
        self.seasons = seasons
    def __str__(self):
            return f"{self.seasons}"
    def predict_fruit(self):
        for item in empty_list:
            if self.seasons == item.season:
                print( f"{item.name} was produced in this {self.seasons} season")
    



#The Legendary African Drum Circles: You're part of a community that hosts one of the largest drum 
#circles in Africa. There are different types of traditional drums used in the circle, each with its 
#unique sound and rhythm. The Djembe, Talking Drum, and Bougarabou are among the popular ones. 
#These drums have common properties such as the material they're made from and their sizes, 
#but they also have distinct characteristics. For instance, the Talking Drum can mimic the lines 
#of human speech, the Djembe is known for its wide range of tones, and the Bougarabou is noted
#for its deep, rich bass tones.
#You want to create a software model of the drum circle that encapsulates these different types of
#drums. You wish to include methods for each drum that represent the sound it makes, and also group
#similar drums together. Think about creating a base Drum class that contains properties and methods 
#common to all drums, and then create subclasses for each specific type of drum (like Djembe, Talking Drum, 
#and Bougarabou).
#The subclasses should inherit from the base Drum class and also implement their unique characteristics. This software model would help newcomers understand the characteristics of each drum and how they contribute to the overall rhythm of the drum circle.

class Drum:
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def makeSound(self,tones):
        print(f"The drum makes {tones}")
class Djembe(Drum):
    def makeSound(self,tones):
        print(f"The Djembe drum makes {tones} ")
class TalkingDrum(Drum):
    def makeSound(self,tones):
        print(f"The drum makes {tones}")
class Bougarobou(Drum):
    def makeSound(self,tones):
        print(f"The Bougarabou drum makes {tones}")

drum=Drum("wood","large")
drum.makeSound("du du du")

djembe=Djembe("leather","medium")
djembe.makeSound("High,medium,low")

talkingDrum=TalkingDrum("plastic","small")
talkingDrum.makeSound("Mimics human speech")

bougarabou=Bougarobou("synthetic fibre","extra large")
bougarabou.makeSound("rich bass")
print(bougarabou.material)

#mentor oop questions


class FusionCuisine:
    def __init__(self,cooking_temperature,combined_ingredients,time):
        self.combined_ingredients=combined_ingredients
        self.cooking_temperature=cooking_temperature
        self.time=time
    def predict_taste_and_texture(self):
        if self.cooking_temperature==75:
            if self.combined_ingredients=="Rice,ginger and garlic" and self.time=="8 pm":
                return f"The food cooked is Pilau, taste is spicy and texture is course  "
            if self.combined_ingredients=="Pork,potatoes and garlic" and self.time=="2 pm":
                return f"The food coked is Mashed potatoes with grilled pork, taste is smoky_spicy and texture is course"
        if self.cooking_temperature==60 :
            if self.combined_ingredients=="fish, coconut milk and tomatoes" and self.time== "7 pm":
                return f"The food cooked is grilled fished, taste is creamy-salty and texture is soft"
        else:
            return f"Every food has its own temperature, ingredients and time"

cuisine1=FusionCuisine(75,"Rice,ginger and garlic","8 pm")
cuisine2=FusionCuisine(75,"Pork, potatoes and garlic","2 pm")
cuisine3=FusionCuisine(60,"fish, coconut milk and tomatoes","7 pm")
cuisine4=FusionCuisine(20,"Pork, potatoes and garlic","1 pm")
print(cuisine1.predict_taste_and_texture())
print(cuisine2.predict_taste_and_texture())
print(cuisine3.predict_taste_and_texture())
print(cuisine4.predict_taste_and_texture())

# Output The food cooked is Pilau, taste is spicy and texture is course


#Take 10 integer inputs from user and store them in a list. Again ask user
#to give a number. Now, tell user whether that number is present in list 
#or not. ( Iterate over list using while loop ).

def print_numbers():
    num=20
    number_list=[]
    number=input()
    if num in number_list:
        number_list.append(number)
        print(f"Yes")
    else:
        print(f"No")
    #while num>0:
       # print (f"Enter number")
       # number=input()
       # number_list.append(number)
      #  i=1-i
     #   print (f"Enter a number")
    #num2=input()
    #i=9
    #count=0
    #while i>=0:
     #   if num2==num[i]:
    #        print(f"Yes it is present")
   #         count=count
  #          i=i-1
 #       if count==0:
#            print(f"No, the number is not present")
print_numbers()


# class Story:
#    def __init__(self, title, age_group, moral_lesson, length, language):
#        self.title = title
#        self.age_group = age_group
#        self.moral_lesson = moral_lesson
#        self.length = length
#        self.language = language
#        self.published = False


#    def publishStory(self):
#        self.published = True
#        if self.published:
#            print(f"The story '{self.title}' has been published.")
#        else:
#            print(f"The story '{self.title}' has not been published yet.")




# class StoryTeller:
#    def __init__(self, name):
#        self.name = name
#        self.stories = []


#    def addNewStory(self, title, age_group, moral_lesson, length, language):
#        story = Story(title, age_group, moral_lesson, length, language)
#        self.stories.append(story)
#        print(f"The story '{title}' has been narrated by {self.name} and now is in her list.")




# class Translator(Story):
#    def __init__(self, title, age_group, moral_lesson, length, language):
#        super().__init__(title, age_group, moral_lesson, length, language)


#    def translateStory(self, newLanguage):
#       print(f"The story '{self.title}' is being translated to {newLanguage}.")
#       if self.language != newLanguage:
#            self.language = newLanguage
#            print(f"The story '{self.title}' has been translated to {newLanguage}.")
#       else:
#            print(f"The story '{self.title}' is already in {newLanguage}. No translation needed.")

# storyteller = StoryTeller("Sonia")
# storyteller.addNewStory("Born Again", "20-23", "Knowing your self-worth", "10min", "English")
# storyteller.addNewStory("The Journey", "18-25", "Finding inner strength", "15 min", "English")
# translator = Translator("Born Again", "20-23", "Knowing your self-worth", "10min", "English")
# print(translator.translateStory("Kiswahili"))
# print(storyteller.addNewStory("Born Again","10-15","We should believe in Christ","2 hrs long","English"))


# Q3. **Wildlife Preservation:** You're a wildlife conservationist working on a program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# These classes might relate to each other through inheritance

# class Species:
#     def __init__(self,diet,life_span,migration_pattern):
#         self.diet={
#             "carnivore":"meat",
#             "herbivore":"grass",
#             "omnivore":"grass and meat"
#                    }
#         self.life_span=life_span
#         self.migration_pattern=migration_pattern
#     def seeDiet(self,animal):
#         animal_category={
#             "carnivores":"Lions,jackal,leopards,cheetah",
#             "herbivores":"Zebras,antelopes,deer,buffalo",
#             "omnivores":"Elephants,hippopotamus"
#         }
#         for animal in animal_category:
#             if animal in animal_category:
#                 return f"This animal eats meat"
#             elif anim
# species=Species("meat",5,"Migrate twice a year")
# print(species.seeDiet("Zebra"))
# print(species.animal_category.index[2])

# class Species:
#     def __init__(self, name, diet, lifespan):
#         self.name = name
#         self.diet = diet
#         self.lifespan = lifespan
#     def display_info(self):
#         print(f"Species: {self.name}, Diet: {self.diet}, Lifespan: {self.lifespan} years")
#     def is_endangered(self):
#         if self.lifespan < 5:
#             return True
#         else:
#             return False
# class Predator(Species):
#     def __init__(self, name, diet, lifespan, hunting_method):
#         super().__init__(name, diet, lifespan)
#         self.hunting_method = hunting_method
#     def display_info(self):
#         super().display_info()
#         print(f"Hunting Method: {self.hunting_method}")
#     def hunt(self, prey):
#         print(f"{self.name} is hunting {prey.name} using {self.hunting_method}!")
# class Prey(Species):
#     def __init__(self, name, diet, lifespan, migration_pattern):
#         super().__init__(name, diet, lifespan)
#         self.migration_pattern = migration_pattern
#     def display_info(self):
#         super().display_info()
#         print(f"Migration Pattern: {self.migration_pattern}")
#     def migrate(self):
#         print(f"{self.name} is migrating according to its {self.migration_pattern} migration pattern!")
# tiger = Predator("Lion", "Carnivore", 5, "Ambush hunting")
# zebra = Prey("Gazelle", "Herbivore", 7, "Seasonal migration")
# tiger.display_info()
# print()
# zebra.display_info()
# print()
# if tiger.is_endangered():
#     print(f"{tiger.name} is an endangered species.")
# else:
#     print(f"{tiger.name} is not an endangered species.")
# if zebra.is_endangered():
#     print(f"{zebra.name} is an endangered species.")
# else:
#     print(f"{zebra.name} is not an endangered species.")
# print()
# tiger.hunt(zebra)
# zebra.migrate()

class Story:
   def __init__(self, title, age_group, moral_lesson, length, language):
       self.title = title
       self.age_group = age_group
       self.moral_lesson = moral_lesson
       self.length = length
       self.language = language
       self.published = False


   def publishStory(self):
       self.published = True
       if self.published:
           print(f"The story '{self.title}' has been published.")
       else:
           print(f"The story '{self.title}' has not been published yet.")




class StoryTeller:
   def __init__(self, name):
       self.name = name
       self.stories = []


   def addNewStory(self, title, age_group, moral_lesson, length, language):
       story = Story(title, age_group, moral_lesson, length, language)
       self.stories.append(story)
       print(f"The story '{title}' has been written by {self.name}.")




class Translator(Story):
   def __init__(self, title, age_group, moral_lesson, length, language):
       super().__init__(title, age_group, moral_lesson, length, language)


   def translateStory(self, newLanguage):
       print(f"The story '{self.title}' is being translated to {newLanguage}.")
       if self.language != newLanguage:
           self.language = newLanguage
           print(f"The story '{self.title}' has been translated to {newLanguage}.")
       else:
           print(f"The story '{self.title}' is already in {newLanguage}. No translation needed.")




storyteller = StoryTeller("Sonia")
storyteller.addNewStory("Born Again", "20-23", "Knowing your self-worth", "10min", "English")
storyteller.addNewStory("The Journey", "18-25", "Finding inner strength", "15 min", "English")


translator = Translator("Born Again", "20-23", "Knowing your self-worth", "10min", "English")
translator.translateStory("Kiswahili")


print(storyteller.stories)




class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
    def display_info(self):
        print(f"Species: {self.name}, Diet: {self.diet}, Lifespan: {self.lifespan} years")
    def is_endangered(self):
        if self.lifespan < 5:
            return True
        else:
            return False
class Predator(Species):
    def __init__(self, name, diet, lifespan, hunting_method):
        super().__init__(name, diet, lifespan)
        self.hunting_method = hunting_method
    def display_info(self):
        super().display_info()
        print(f"Hunting Method: {self.hunting_method}")
    def hunt(self, prey):
        print(f"{self.name} is hunting {prey.name} using {self.hunting_method}!")
class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern):
        super().__init__(name, diet, lifespan)
        self.migration_pattern = migration_pattern
    def display_info(self):
        super().display_info()
        print(f"Migration Pattern: {self.migration_pattern}")
    def migrate(self):
        print(f"{self.name} is migrating according to its {self.migration_pattern} migration pattern!")
tiger = Predator("Lion", "Carnivore", 5, "Ambush hunting")
zebra = Prey("Gazelle", "Herbivore", 7, "Seasonal migration")
tiger.display_info()
print()
zebra.display_info()
print()
tiger.hunt(zebra)
zebra.migrate()



# Write a Python function student_data () that will print the ID of a student (student_id). 
# If the user passes an argument student_name or student_class the function will print the student 
# name and class.
class StudentData:
    def  __init__(self,id,name,student_class):
        self.id=id
        self.name=name
        self.student_class=student_class

    def printInfo(self,student_name):
        if len(student_name)!=0 and self.name==student_name:
            return f"Student {self.name} has this information:\n Id:{self.id} \n Class:{self.student_class}"
        else:
            return f"Not registered"

studentOne=StudentData("JK0938","Arsen","Hopper")
studentTwo=StudentData("9382021","Kabanyana","A")
studentThree=StudentData("0012021","Samuel","B")
studentFour=StudentData("0022021","Arstide","C")
studentFive=StudentData("0032021","John","Hopper")
print(studentOne.printInfo("Arseny"))
print(studentTwo.printInfo("Kabanyana"))
print(studentThree.printInfo("Sammy"))
print(studentFour.printInfo("Arstide"))
print(studentFive.printInfo("Arseny"))


