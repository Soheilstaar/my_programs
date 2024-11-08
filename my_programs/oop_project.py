
# we import all functions from bank_account class

from bank_accounts import *

# here we create objects for bankAccount class

soheil= BankAccount (1000,'Soheil')
mahsa= BankAccount (2000,'Mahsa')

soheil.get_balance()
mahsa.get_balance()

soheil.deposit(500)
mahsa.deposit(500)

soheil.withdraw(1000)
mahsa.withdraw (10)

soheil.transfer(1000000,mahsa)
soheil.transfer(120,mahsa)

luca= InterestRewardAcct (1000,'Luca')
luca.deposit (100)
luca.get_balance()