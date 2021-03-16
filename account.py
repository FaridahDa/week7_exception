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
        if (self.balance - amount) < 0:
            print("declined")
            raise InsufficientFundsException("could not complete transaction, insufficient funds") #the err argument came from here
        #insufficient funds is a class - when we raise it - we are creating the object - what ever we put in the bracket is going to be an arugment of that object
        #class throws error in the air and client script is going to catch the error thats why it is ebing raised here
        #try except is being implemented in the client script
        else:
            print("not an error")
            return self.balance



        # try:
        #     self.balance -= amount
        # except InsufficientFundsException:
        #     print(f"You have insufficient funds in your account to withdraw £{amount}\n" + f"Your current balance is £{self.balance}, you will be overdrawn by £ {abs(self.balance - amount)}.Please check you have funds available in your account before processing this transaction")
        #
        # else:
        #     return f"You have successfully withdrawn £{amount}, your new balance is {self.balance}"


            # return f"You have successfully withdrawn £{amount}, your new balance is {self.balance}"

        # if (self.balance - amount) < amount:
            # raise InsufficientFundsException(f"You have insufficient funds in your account to withdraw £{amount}\n" + f"Your current balance is £{self.balance}, you will be overdrawn by £ {abs(self.balance - amount)}.Please check you have funds available in your account before processing this transaction")

    def get_account_details(self):
        return f"The Account for {self.fullname} was opened at {self.branch}\n" + f"Account Number: {self.account_no}\n" + f"Sort Code: {self.sort_code}\n" + f"The Balance today is £{self.balance}"
#
# ac1 = Account("Faridah Dada","40 04 15", "7567860", "Westfield Stratford", 500)
# print(ac1.withdraw(600))
# (a,b) = (6,0)
# try:# simple use of try-except block for handling errors
#     g = a/b
# except ZeroDivisionError:
#     print ("This is a DIVIDED BY ZERO error")

