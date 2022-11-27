#Inheritance Super/sub classes(Single, multiple,hierachical /

class FarmAnimals:
    def __init__(self, name, age):
        self.name = name
        self.age=age
        
        print("")
    def show(self):
     print(f"On my farm i have{self.name} aged {self.age} years")
    
class Cow(FarmAnimals):
    def __init__(self, name, age,color):
        super.__init__(name,age)   #super means the parent or 
        #super class FarmAnimal from which the cow inherits the name & age attributes.
        self.color =color
    def speak (self):
        print("Mooo!!")
    
class Goats(FarmAnimals):
    def speak(self):
        print("Meeehhhehh")
FarmA= FarmAnimals('Magajuu' ,8)
FarmA.show()
print('_____________________________________')