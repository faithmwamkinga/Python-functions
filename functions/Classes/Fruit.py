class Fruits():
    category="Vitamins"
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste
    def wash(self):
        print(f"The {self.name} is being washed")
    def count(self):
        print(f"There are 10 {self.color} {self.name}")
    def peel(self):
        print(f"The {self.name} is being peeled now and it is {self.taste}")


