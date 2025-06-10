class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
            

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_balance(self, current_balance=0):
        current_balance = self.balance if current_balance == 0 else current_balance
        print(f"Current Balance: ${current_balance:.2f}")
        return self.balance
        

    def __str__(self):
        return f"Account Balance: {self.balance}"
    
    