from square import Shape
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
x = int(input("Enter length: "))
y = int(input("Enter width: "))
s = Rectangle(x,y)
s.area()