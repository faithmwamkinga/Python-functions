class Car:
    make="BMW"
    def __init__(self,model,color,mileage):
        self.model=model
        self.color=color
        self.mileage=mileage
    def start(self):
        print(f" {self.model} starts from 0km/hr")
    def drive(self):
        print(f"{self.model} car drives")
    def stop(self):
        print(f"{self.model} is stopping at Mombasa")
# car1=Car("BMWX7","White","200km/hr")
# car2=Car("BMWXi","Black","260km/hr")
