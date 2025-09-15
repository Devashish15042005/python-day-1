class BankAccount:
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"{self.account_name} :Deposite : {amount} New Balance: {self.balance}")
        return self
    def withdraw(self,amount):
        self.balance -= amount
        if amount > self.balance:
         print(f"{self.account_name}: Insufficient balance")
        else:
           print(f"{self.account_name}: Withdraw: {amount} New balance: {self.balance}")
        return self
    def showbalance(self):
        print(f"{self.account_name} Balance: {self.balance}")
        return self
class SavingsAccount(BankAccount):
    def __init__(self, account_name, balance=0,withdraw_limit = 1000):
        super().__init__(account_name, balance)
        self.withdraw_limit = withdraw_limit
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"{self.account_name} Cannot Withdraw Over the {self.withdraw_limit} at once!")
        else:
            super().withdraw(amount)
        return self
class CurrentAccount(BankAccount):
    def __init__(self, account_name, balance=0,overdraft = 500):
        super().__init__(account_name, balance)
        self.overdraft = overdraft
    def withdraw(self,amount):
        if amount > self.balance + self.overdraft:
            print(f"{self.account_name}: Exceeds overdraft limit! {self.overdraft}")
        else:
            self.balance-= amount
            print(f"{self.account_name}: Withdraw : {amount} New Balance : {self.balance}")
        return self
print("------- Savings Account Example-------")
s_acc = SavingsAccount("Devashish Savings",2000)
s_acc.deposite(500).withdraw(1200).withdraw(800).showbalance()
print("-------Current Account Example-------")
c_acc = CurrentAccount("Devashish Current",1000)
c_acc.deposite(500).withdraw(1800).withdraw(300).showbalance()