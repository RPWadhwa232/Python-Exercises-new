
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

class Dog(Animal): #Inheritance example
    species = "Dog"

    def __init__(self, name, color):
        self.name = name
        self.color = color

dog1 = Dog("Loki", "Green")
print(dog1.color)

""""
dog = Animal("Rex", "Dog", "Brown")
dog.getName() # substitue fo print command

print(dog.name, dog.species, dog.color)



# dog.name()
# dog.nameFunction("Zorro")

"""
"""
import datetime
x = datetime.datetime.now()

print(x)

class Bank_account:
    Name = ""
    dob = ""
    Address = ""
    Account = ""

    def account_holder_detail(self, customer_name, date_of_birth, customer_address, Account_Number):
        self.Name = customer_name
        self.dob = date_of_birth
        self.Address = customer_address
        self.Account = Account_Number

user1 = Bank_account()
user2 = Bank_account()
user3 = Bank_account()

user1.Account = 12322450

user1.Name = "John Smith"
user2.Name = "R Wadhwa"
user3.Name = "Kay Johnson"

print(user1.Name)
print(user2.Name)
print(user3.Name)
print(user1.dob)

print(user1.Account)

"""








