#write a program to create a class point that consists of a constructor to set coordinates = x and y.
#also it consists of a function that returns the coordinates in point format.
#create an object passing the coordinates and print the point.
class point:
    def __init__(self,X=0,Y=0):
        self.X=X
        self.Y=Y
    def __str__(self):
        return f"({self.X},{self.Y})"
ob=point(35,67)
print(ob)