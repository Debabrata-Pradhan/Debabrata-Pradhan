class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []
        self.pin = None  # Initialize PIN (you can set it later)

    def account_balance(self): # Returns the account balance.
        return self.balance

    def cash_withdrawal(self, amount): # Withdraws cash from the account.
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def cash_deposit(self, amount): # Deposits cash into the account.
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def change_pin(self, new_pin): # Changes the PIN.
        self.pin = new_pin
        return "PIN changed successfully."

    def get_transaction_history(self): # Returns the transaction history.
        return self.transaction_history

# Example usage:
atm = ATM()
print(atm.cash_deposit(100))
print(atm.cash_withdrawal(50))
print(atm.account_balance())
print(atm.get_transaction_history())