class Animal:
    name = ""
    species = ""
    color = ""

    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color
  

    def nameFunction(self,nameofanimal:str):
        self.name = nameofanimal
    
    def getName(self): 
        print("Name is: " + self.name)
    def speak(self):
        print("bark")

class Dog(Animal):
    species = "Dog"

    def __init__(self, name, color):
        self.name = name
        self.color = color

loki = Dog("Loki", "Green")
loki.speak()