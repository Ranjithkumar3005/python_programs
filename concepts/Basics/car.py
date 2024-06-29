class Car:
    
    wheels=4 #class variable
    def __init__(self,model,person) :
        self.model=model#instance variable
        self.person=person
    
    def model_car(self):
        return "The model of the car is "+self.model
        
    def drive(self):
        print("The car is driving by "+self.person)