class CheckingAccount:
    def __init__(self, accountNumber, accountHolderName, balance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.balance = balance

    def changeName(self):
        self.accountHolderName = input("Enter the new account holder's name: ")
        print("The new account holder is", self.accountHolderName)

    def deposit(self):
        depositAmount = float(input("Enter the amount to deposit: "))
        if depositAmount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += depositAmount

    def withdraw(self):
        withdrawalAmount = float(input("Enter the amount to withdraw: "))
        if withdrawalAmount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= withdrawalAmount

    def printData(self):
        print("Account number:", self.accountNumber)
        print("Account holder's name:", self.accountHolderName)
        print("Balance:", self.balance)
        print(" ")


account1 = CheckingAccount("3", "Felipe", 200)

account1.printData()
account1.withdraw()

account1.printData()