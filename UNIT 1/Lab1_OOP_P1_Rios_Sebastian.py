class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")

    def check_balance(self):
        print(f"Current balance is {self.__balance}")


BankAccount1 = BankAccount("Raul Perez", 5000)
BankAccount2 = BankAccount("Joel Lopez", 3000)

# Operaciones Raul
print(f"Titular: {BankAccount1.holder}")
BankAccount1.check_balance()
BankAccount1.deposit(1000)
BankAccount1.withdraw(2000)
BankAccount1.check_balance()

# Operaciones Joel
print(f"Titular: {BankAccount2.holder}")
BankAccount2.check_balance()
BankAccount2.deposit(5000)
BankAccount2.withdraw(2000)
BankAccount2.check_balance()
