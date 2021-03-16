import random
from account_errors import InsufficientFundsException
class Account:
    no_created = 0
    def __init__(self, fullname,sort_code, account_no, branch, balance):
        self.fullname = fullname
        self.sort_code = sort_code
        self.account_no = account_no
        self.branch = branch
        self.balance = balance
        Account.no_created +=1

    #def __str__(self):
        #return f"The Account for {self.fullname} was opened at {self.branch}\n." + f"Account Number: {self.account_no}\n"  + f"Sort Code: {self.sort_code}\n" + f" The Balance today is {self.balance}"

    def get_branch_location(self):
        return self.branch

    def get_account_no(self):
        return self.account_no

    def get_sort_code(self):
        return self.account_no

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return f"Your current balance is £{self.balance}"

    def withdraw(self, amount):
        #self.balance -= amount
        #return f"You have successfully withdrawn £{amount}, your new balance is {self.balance}"
        if (self.balance - amount) < amount:
            raise InsufficientFundsException(f"You have insufficient funds in your account to withdraw £{amount}\n" + f"Your current balance is £{self.balance}, you will be overdrawn by £ {abs(self.balance - amount)}.Please check you have funds available in your account before processing this transaction")

    def get_account_details(self):
        return f"The Account for {self.fullname} was opened at {self.branch}\n" + f"Account Number: {self.account_no}\n" + f"Sort Code: {self.sort_code}\n" + f"The Balance today is £{self.balance}"

ac1 = Account("Faridah Dada","40 04 15", "7567860", "Westfield Stratford", 500)
print(ac1.get_account_details())

