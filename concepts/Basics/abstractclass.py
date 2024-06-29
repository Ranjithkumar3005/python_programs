#a class is contain one or more abstarct methods
#a method is only declarartion not a implementation
from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
    
class a(vehicle):
    def drive(self):
        print("a")
        
b=a()
b.drive()


foods=list()
while food := input("Enter the food:")!="quit":
    foods.append(food)
    
print(foods[0])