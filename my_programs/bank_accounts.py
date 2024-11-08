# OOP Project !

class BalanceException(Exception):
    pass

class BankAccount:

    # here we state the attributes for our object 
    def __init__ ( self, initialAmount, acctName):
        self.balance= initialAmount
        self.name= acctName
        print(f"\nAccount '{self.name}' Created!\nBalance: ${self.balance:.2f}\n")
    # here we state the actions (methods) for our object 
    def get_balance(self):
        print(f"\nAccount '{self.name}'Balance = ${self.balance:.2f}\n")


    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete!")
        self.get_balance()

# here we check if the amount in the account can be withdrawn or not by raising the error we defined in the BalanceException class.

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry! Account '{self.name}' has only a balance of ${self.balance:.2f}")
        
# here we define withdraw function and we check if it can be done or we need to have an error shown instead. we use 'try' to raise an exception if error was found.

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance= self.balance - amount
            print('\nWithdraw Complete!')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted! {error}")

    def transfer(self, amount, account):
        try:
            print('\n**************\n\nBeginning Transfer!')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete!\n**************\n\n')
        except BalanceException as error:
            print(f"\nDeposit interrupted! \n{error}\n******************")

class InterestRewardAcct(BankAccount):
    def deposit(self,amount):
        self.balance= self.balance + (amount * 1.05)  
        print('\nDeposit Completed')
        self.get_balance()        

