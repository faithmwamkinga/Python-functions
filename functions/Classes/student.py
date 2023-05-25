class Student:
    # name="Elizabeth"
    # age=22
    # Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
            #  - show_full_name
            #  - year_of_birth
            #  - show_initials
    school="Akirachix"
    #def init is a constructor that is used to ini
    # declare attributes for class objects 
#self is used for inheritance
    def __init__(self,firstname,secondname,age,nationality):
        self.firstname=firstname
        self.secondname=secondname
        self.age=age
        self.nationality=nationality
    def greet_student(self):
        return f"Hello {self.firstname} {self.secondname} {self.school}"
    def year_birth(self):
        year=2023-self.age
        return f" Hello {self.name}, you were born in {year}"
    def initials(self,firstname,secondnanme):
        first_initial=firstname[0]
        lastname_initial=secondnanme[0]
        #alternative print
        print(f"The initials are {first_initial}.{lastname_initial}")
    
    # nationality="Tanzanian"

#Instance variables to make objects with dynamic values




