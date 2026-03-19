import math
class Point:
    x = int
    y = int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return"(%d,%d)" %(self.x, self.y)

    def Read(self):
        self.x = int(input("input x: "))
        self.y = int(input("input y: "))
    
    def distance(self, point):
        d = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return d
    

diemA = Point(3,4)
print(diemA)

diemB = Point()
diemB.Read()
print(diemB)

diemC = Point(-diemB.x, -diemB.y)
print(diemC)

print(diemB.distance(diemC))

diemO = Point(0, 0)
print(diemB.distance(diemO))