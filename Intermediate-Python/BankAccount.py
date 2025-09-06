class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance = 0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    #Record initial deposit if any
        if initial_balance > 0:
            self.transaction_history.append(f"Initial Desposit: + ${initial_balance:.2f}")

    def deposit(self, amount):
        #Adding money to the account(must be positive)
        if amount <= 0:
            print('Error! Deposit amount must be positive')
            return False
        
        self.balance += amount
        self.transaction_history.append(f"Desposit + ${amount:.2f}")
        print(f"Your account has been deposited by:$ {amount:.2f}")
        print(f'New Balance: {self.balance:.2f}')
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal must be positive!")
            return False
        
        if amount > self.balance:
            print(f'Error! insufficient Balance Available: ${amount:.2f}')
            return False
        
        self.balance -= amount 
        self.transaction_history.append(f'Successful Cash withdrawal: ${amount:.2f}')
        print(f"Amount withdrawn successfully: ${amount:.2f}")
        print(f"Remaining Balance: {self.balance:.2f}")
        return True
    
    def get_balance(self, amount):
        #Return the current balance
        return self.balance
    
    def transfer(self, other_account,amount):
        if amount <= 0:
            print("Error! Transfer must be a positive number")
            return False

        if amount > self.balance:
            print(f"Insufficient amount: {self.balance:.2f}")

        #Withdraw from this account:
        self.balance -= amount
        self.transaction_history.append(f"Transfer out to: {other_account.account_holder} : -${amount:.2f}")
        
        other_account.balance -= amount
        other_account.transaction_history.append(f"Transfer in from: {self.account_holder}: ${amount:.2f}")
        print(f"Your remaining balance: {self.balance:.2f}")
        return True
    
    def get_account_info(self):
        print(f"======Account Information======")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current balance: {self.balance:.2f}")

    def show_transaction_history(self):
        print(f"====Transaction History for {self.account_holder}====")
        if not self.transaction_history:
            print("No Transactions Yet")
        else:
            for i, transaction in enumerate(self.transaction_history,1):
                print(f"{i}.{transaction}")
            print(f"Current Balance: ${self.balance:.2f}")

# Test the BankAccount system
print('===== BANK ACCOUNT SYSTEM DEMO=====\n') 

#Create Bank accounts:
account1 = BankAccount('Fatima Ali','A00023',95.20)
account2 = BankAccount('Abdul rehman','A00012',10.60)
account3 = BankAccount('Nasir Ali','A00061',150.45)
account4 = BankAccount('Jazia Nasir','A00055',35.22) 
print('=====Accounts Created=====\n') 

#Deposit Amount:
print('=====Testing Deposits=====\n')
account1.deposit(-3)
account2.deposit(5)
account3.deposit(20)
account4.deposit(10)


#Withdraw the amount
print('=====Testing Cash Withdrawals=====')
account1.withdraw(10)
account2.withdraw(5)
account3.withdraw(60)
account4.withdraw(2)

#Amount Transfer
print('=====Testing amount Transferring=====')
account1.transfer(account4,20)
account3.transfer(account2,10)
print()

#Get the Account Info
print('=====Testing Account Info=====\n')
account1.get_account_info()
account2.get_account_info()
account3.get_account_info()
account4.get_account_info()

#Show transaction history
print('=====Testing Transaction History=====')
account1.show_transaction_history()
account2.show_transaction_history()
account3.show_transaction_history()
account4.show_transaction_history()



    