

# Challenge - 4) Implement a Banking Account
class Account:

    def __init__(self,title = None, Balance = 0):
        self.title = title
        self.Balance = Balance


class SavingsAccount(Account):

        def __init__(self,title = None,Balance = 0,interestRate = 0):
                super().__init__(title, Balance) 
                self.interestRate = interestRate


        def __str__(self):
                return f"\ntitle: {self.title} \nBalance: {self.Balance} \ninterestRate: {self.interestRate}"

Obj = SavingsAccount("Ashish",5000,5)
print(Obj)