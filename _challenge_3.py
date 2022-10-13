



# Challenge -3) Implement the Complete Student Class

         
class Student:
        self.__name = name
        self.__rollNumber=rollNumber

        def setName(self,name):
                self.name = name

        def getName(self):
                return self.name
        
        def setRollNumber(self,rollNumber):
                self.rollNumber = self.rollNumber
                
        
        def getRollNumber(self):
                return self.rollNumber

        def display(self):
                return f"\nname: {self.name} \nrollNumber: {self.rollNumber}"

Obj = Student("Raj")
print(Obj.display())

Obj.setName("Yash")
print(Obj.getName())

Obj.setRollNumber("25")
print(Obj.getRollNumber())
 
print(Obj.display())