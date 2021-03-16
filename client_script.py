from account_errors import InsufficientFundsException
from customer import Customer
from savings_account import Savings_account
from current_account import Current_account

jessie_savings = Savings_account(500, 2.5, 3, 2)
jessie_savings.withdraw(300)
print(jessie_savings.get_balance())
jessie_savings.withdraw(500)

asia_current = Current_account(1000, -500, 500)
print(asia_current.get_balance())
print(asia_current.send_money(100, "jessie"))
print(asia_current.get_balance())
asia_current.send_money(3000, "jackie")
asia_current.receive_money(50, "jessie")
print(asia_current.get_balance())


