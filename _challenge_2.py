


# Challenge- 2) Implement a Calculator Class

# Sample input

# obj = Calculator(10, 94)
# obj.add()
# obj.subtract()
# obj.multiply()
# obj.divide()

# Sample output:
#     104
#     84
#     940
#     9.4                 

class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        print(self.num1 + self.num2)
        
    def subtract(self):
        print(self.num2 - self.num1)
        
    def multiply(self):
        print(self.num1 * self.num2)
        
    def divide(self):
        print(self.num2 / self.num1)

cal_Obj= Calculator(10, 94)
cal_Obj.add()
cal_Obj.subtract()
cal_Obj.multiply()
cal_Obj.divide()