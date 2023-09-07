class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited {amount} units. New balance: {self.__account_balance}"
        else:
            return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew {amount} units. New balance: {self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."
    
    def display_balance(self):
        return f"Account balance: {self.__account_balance}"

# Creating an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000)

# Testing deposit and withdrawal functionality
print(account.deposit(500))
print(account.withdraw(200))
print(account.display_balance())