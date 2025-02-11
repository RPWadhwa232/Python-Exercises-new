class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
            
        print(f"£{amount} has been added to {self.account_holder}'s account. New balance is £{self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def check_the_balance(self, amount):
        self.balance = amount


account1 = BankAccount("RP", 100)
account1.deposit(20)


