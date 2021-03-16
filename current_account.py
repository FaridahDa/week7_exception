from account_errors import InsufficientFundsException
from account import Account
class Current_account(Account):
    def __init__(self,fullname, balance, overdraft,spend_limit):
        Account.__init__(self,fullname, balance)
        self._overdraft = overdraft
        self._spend_limit = spend_limit

    def __str__(self):
        super().__str__()
        return f"Overdraft: {self._overdraft}\n" + f"Spending Limit: {self._spend_limit}"

    def send_money(self, amount, recipient):
        if amount < self._spend_limit:
            self.balance -= amount
            return f"you have sent £{amount} to {recipient}"
        else:
            return f"Could not send £{amount} to {recipient}, as it is larger than your spending limit of £{self._spend_limit}"

    def receive_money(self, amount, recipient):
        self.balance += amount
        return f"you have received £{amount} from {recipient}"

    def make_withdrawal(self, amount):
        if self.balance - amount <= self._overdraft:
            raise InsufficientFundsException(f"You have insufficient funds in your account to make the withdraw of £{amount}. Please Check you have the funds available in your account before making this withdraw")

ac1 = Current_account("Faridah Dada", 50, 20,100)
print(ac1.make_withdrawal(500))