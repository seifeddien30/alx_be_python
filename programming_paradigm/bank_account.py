class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

# Sample usage for debugging:
if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.display_balance()
    success = account.withdraw(30)
    print(f"Withdraw successful: {success}")
    account.display_balance()
    success = account.withdraw(150)
    print(f"Withdraw successful: {success}")
    account.display_balance()
