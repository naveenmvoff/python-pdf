#  Implement a program that simulates a basic bank account using a BankAccount class.

class BankAccount:
    def __init__(self, owner, balance=0):
        """Initialize the bank account with an owner and an optional initial balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the bank account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the bank account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def __str__(self):
        """Return a string representation of the account."""
        return f"BankAccount(owner: {self.owner}, balance: ${self.balance})"


# Example usage:
if __name__ == "__main__":
    # Creating an account for a person named "Naveen" with an initial balance of 1000
    account = BankAccount("Naveen", 1000)

    # Checking balance
    print(account)

    # Depositing money
    account.deposit(500)

    # Withdrawing money
    account.withdraw(300)

    # Trying to withdraw more than the current balance
    account.withdraw(1500)

    # Final balance
    print(f"Final balance: ${account.get_balance()}")