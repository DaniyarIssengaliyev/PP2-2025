class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, end = " ")
        print(self.y)

    def move(self, x1,y1):
        self.x += x1
        self.y += y1
        print(self.x, end = " ")
        print(self.y)
    def dist(self, Point):
        print(abs(Point.x - self.x), end = " ")
        print(abs(Point.y - self.y))
p1 = Point(10,5)
p2 = Point(4, 2)

p1.show()
p2.show()
p1.move(2,3)
p1.dist(p2)