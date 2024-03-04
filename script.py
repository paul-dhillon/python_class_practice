# 1 create a BankAccount class with the attributes of interest rate and balance
class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    def __str__(self):
        return f"Interest rate: {self.interest_rate}, Account Balance: {self.balance}"

    # 2 Create a deposit method
    def deposit(self, amount):
        self.balance += amount
        return self

        # 3 Create a Withdraw method

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(f"New Balance after fee: {self.balance}")
        return self

        # 4 Create a display account method

    def display_account_info(self):
        print(f"Current Balance: ${self.balance}")
        return self

        # 5 Create a yield interest method

    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance * self.interest_rate
        else:
            print("No Interest earned due to insufficient funds")
        return self


# 6 create two different accounts
account1 = BankAccount(interest_rate=0.02, balance=1500)
account2 = BankAccount(interest_rate=0.018, balance=0)


# 7 Chaining class methods
account1.deposit(500).withdraw(300).deposit(150).deposit(
    85
).yield_interest().display_account_info()

print(account1)

account2.deposit(3000).deposit(1500).withdraw(300).withdraw(450).withdraw(50).withdraw(
    125
).yield_interest().display_account_info

print(account2)
