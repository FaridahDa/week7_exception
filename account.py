import random
class Account:
    no_created = 0
    def __init__(self, fullname, balance):
        self.fullname = fullname
        self.sort_code = "40 04 15"
        self.account_no = random.randint(100000, 999999)
        self.branch = "Westfield Stratford Branch"
        self.balance = balance
        Account.no_created +=1

    def __str__(self):
        return f"The Account for {self.fullname}was opened at {self.branch}\n." + f"Account Number: {self.account_no}\n"  + f"Sort Code: {self.sort_code}\n" + f" The Balance today is {self.balance}"

    def get_branch_location(self):
        return self.branch

    def get_account_no(self):
        return self.account_no

    def get_sort_code(self):
        return self.account_no

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        return f"You have successfully withdrawn £{amount}, your new balance is {self.balance}"

    def get_balance(self):
        return f"Your current balance is £{self.balance}"



