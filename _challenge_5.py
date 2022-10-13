
# Challenge 5: Handling a Bank Account



class Account:

        
    def __init__(self, title=None, balance=0):
            self.title = title
            self.balance = balance
            # self.v =v
            print("\nTotal balance: ",self.balance)

    def deposit(self,amount):
            amount = float(input("Enter the amount to deposit: "))
            
            d = self.balance + amount
            print("Total balance: ",d)
     
    
    def withdrawal(self,amount1):
           
            amount1 = float(input("Enter the amount to withdraw: "))
            w = self.balance - amount1
            print("Total balance: ", w)
       
        # def getBalance(self):
        #     return self.balance
       
class SavingsAccount(Account):

    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        i = self.interestRate * self.balance / 100
        print("interestAmount: ",i)

    def __str__(self):
            return f"\ntitle: {self.title} \nBalance: {self.Balance} \ninterestRate: {self.interestRate} \ndeposit: {self.deposit} \nwithdrawal: {self.withdrawal} \ninterestAmount: {self.interestAmount}"


demo1 = SavingsAccount("Ashish", 2000, 5) 
demo1.deposit(amount='')

demo2 = SavingsAccount("Ashish", 2500, 5)
demo2.withdrawal(amount1='')
demo2.interestRate(5)
demo2.interestAmount