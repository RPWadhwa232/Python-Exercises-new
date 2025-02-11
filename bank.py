"""
class BankAccount:
    name = ""
    money = 0
    def __init__(self, name):
        self.name = name
    def addMoney(self, moneytoadd):
        self.money = self.money + moneytoadd
    def addMoney 

"""

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

class Saving(Bank_account):
    Account = "saving_account"
    def __init__(self, saving_account):
        self.Account = saving_account

    def open(self):
        print("doit")
