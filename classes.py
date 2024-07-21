class Account:

    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name                     
        self.balance = balance
    
    def deposit(self,amount): 
        self.balance += amount
        print(f'{amount} successfully deposited\nCurrent balance = {self.balance}')

    def withdraw(self,amount) :
        if (self.balance-1500) >= amount :
            self.balance -= amount
            print(f'Current balance = {self.balance}')
        else:
            print('Insufficient balance!')

    def displayBal(self):
        print (f'Current Balance = {self.balance}')

    def getAccNo(self):
        print (f'Account number = {self.acc_no}')

    def getName(self):
        print (f'Name = {self.name}')

    def __str__(self):
        return f'Account No: {self.acc_no}\nName: {self.name}\nCurrent Balance: {self.balance}'

class Bank:

    allAccounts=[]
    acc_no=0

    def createAcc(self,name,initialAmount):
        if initialAmount>=1500:
            self.acc_no += 1
            userAccount=Account(self.acc_no, name, initialAmount)
            self.allAccounts.append(userAccount)
            print(f'Account created!\nAccount No: {self.acc_no}\nName: {name}\nCurrent Balance: {initialAmount}')
        else:
            ('Initial amount is not satisfied!')
    
    def findAcc(self, acc_no):
        for account in self.allAccounts:
            if account.acc_no == acc_no:
                return account
        return None

    def display_acc(self, num):
        account = self.findAcc(num)
        if account:
            print(account)
        else:
            print(f'Account no. {num} not found!')

    def dep(self, num, amount):
        account = self.findAcc(num)
        if account:
            account.deposit(amount)
        else:
            print(f'Account no. {num} not found!')

    def withd(self, num, amount):
        account = self.findAcc(num)
        if account:
            account.withdraw(amount)
        else:
            print(f'Account no. {num} not found!')

print('\n====== ABC BANK ======')

        
    

    
        

        


