# OOPs - Stands for Object Oriented Programming
# Function - Reusability (Redundancy Reduced)
# Class & Object - BluePrint 
# Pros of OOPs - 
# 1. Reusability
# 2. Managing Complexity
# 3. Extendibilty

class Account:
    # Constructor to initialize account Details
    def __init__(self, account_number, account_holder, balance):
        self.account_holder = account_holder # Encapsulated data
        self.account_number = account_number
        self.balance = balance
    
    # Add money to the account
    def deposite(self, amount):
        # Deposite money into the Amount
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposite {amount}. Now Balance is {self.balance}")
        else:
            print("Deposite Amount Must be Positive")
    
    # Withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance = self.balance - amount
            print(f"{amount} withdraw")
        else:
            print("Insufficient Funds")
    
    # Display the Account detail
    def display(self):
        print(f"Account number: {self.account_number}, Balance: {self.balance}")
        
    
## Inheritance : Savings Account inherits from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest):
        super().__init__(account_number, account_holder, balance)
        self.interest = interest
    # Polymorphism (Poly means Many and morphism means form): Dispaly The Account Details 
    def display(self):
        print(f"Savings Account number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest}%")
        
    def add_interest(self):
        interest = self.balance * self.interest/100
        self.balance += interest
        print(f"Interest Added: {interest}. New balance: {self.balance}")
    
## Inheritance: Current Account inherits from Account
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft):
        super().__init__(account_number, account_holder, balance)
        self.overdraft = overdraft
        
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance = self.balance - amount
            print(f"{amount} Withdraw from Current Account. New Balance: {self.balance}")
        else:
            print("OverDraft Limit exceeded")
    
    def display(self):
        print(f"Current Account: {self.account_number}, Balance: {self.balance}")
        
if __name__=='__main__':
    acc1 = SavingsAccount("SA123", "Mohit Khandale", 10000, 3)
    acc2 = CurrentAccount("CA345", "Arjun Rakte", 100000, 25000)
    
    acc1.deposite(20000)
    acc1.add_interest()
    acc1.display()
    
    acc2.deposite(50000)
    acc2.display()
    acc2.withdraw(125000)
    
## Abstraction in Python is a principle of OOPs that simplifies complex system by focusing on essential characteristics while hiding unnecessary details.
## Encapsulation is a fundamental concept in object-oriented programming that operate on that data into a single unit, know as a class.


