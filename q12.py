class BankAccount:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def change_pin(self, new_pin):
        self.pin = new_pin


class SavingsAccount(BankAccount):
    def __init__(self, pin, interest_rate):
        super().__init__(pin)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount


class FeeSavingsAccount(SavingsAccount):
    def __init__(self, pin, interest_rate, withdrawal_fee):
        super().__init__(pin, interest_rate)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount):
        if amount <= (self.balance - self.withdrawal_fee):
            self.balance -= (amount + self.withdrawal_fee)
        else:
            print("Insufficient funds.")


# Create a BankAccount
account1 = BankAccount(1234)
account1.deposit(1000)
print("Balance:", account1.get_balance())  # Output: Balance: 1000
account1.withdraw(500)
print("Balance:", account1.get_balance())  # Output: Balance: 500

# Create a SavingsAccount
account2 = SavingsAccount(5678, 0.05)
account2.deposit(2000)
print("Balance:", account2.get_balance())  # Output: Balance: 2000
account2.apply_interest()
print("Balance:", account2.get_balance())  # Output: Balance: 2100

# Create a FeeSavingsAccount
account3 = FeeSavingsAccount(9012, 0.03, 10)
account3.deposit(3000)
print("Balance:", account3.get_balance())  # Output: Balance: 3000
account3.apply_interest()
print("Balance:", account3.get_balance())  # Output: Balance: 3090
account3.withdraw(500)
print("Balance:", account3.get_balance())  # Output: Balance: 2580
