



# Challenge- 1) Square Numbers and Return Their Sum

# Sample properties: 1, 3, 5

# Sample method output: 35



class Point:
        
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        square_ = self.x**2, self.y**2, self.z**2
        print(sum(square_))


Point_Ob = Point(1,3,5)
Point_Ob.sqSum()