#  Implement a program that simulates a basic bank account using a BankAccount class.

class Bank:
    def __init__(self, holder_name, st_money=0):
        self.holder_name = holder_name
        self.ac_balance = st_money
    
    def deposit(self, ammount):
        if ammount > 0:
            self.ac_balance += ammount
            print(f"Deposited_money ₹{ammount}, ac_current_balance ₹{self.ac_balance}")

    def withdraw(self, money):
        if money > 0:
            if money <= self.ac_balance:
                self.ac_balance -= money
                print("The withdraw ammount is ₹{money} and the current balance in account is ₹{self.ac_balance}")
    
    def getbalance(self):
        return self.ac_balance
    
    def __str__(self):
        return f"Bank Account owner: {self.holder_name}, Account balance: {self.ac_balance} "
    

if __name__ == "__main__":

    account = Bank("Naveen", 1000)
    print(account)
    
    #deposit
    account.deposit(500)
    
    #withdraw
    account.withdraw(200)

    
