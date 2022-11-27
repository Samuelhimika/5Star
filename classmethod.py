class Person:
    number_of_people = 0 #CLASS ATTRIBUTE affects 
    #the class not to any instance or an object
    
    def __init__(self, name,age):
        self.name =name
        self.age =age
        Person.add_person()
        Person.number_of_people += 1
        
    @classmethod #Decorator
    def number0fpeople(cls): # ClASS METHOD
        return cls.number_of_people
    
    @classmethod 
    def add_person(cls):
        cls.number_of_people +=1
    
    
    
P1=Person('Jimm', 14)
P2=Person('Sam', 17)
P3=Person('Sam', 17)
print("")
 
print(Person.number_of_people )

print("")        
    
        
         