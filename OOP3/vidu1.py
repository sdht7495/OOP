import math
class Point:
    x = int
    y = int

    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def_str_(self):
        return"(%sd,%d)" %(self.x, self.y)

    def read(self):
        self.x = int(input("input x: "))
        self.y = int(input("input y: "))
    
    def distance(self, point):
        d = math.sqrt(self.x - point.x)**2 + (self.y - point.y)
        return d
    

    diemA = Point(3,4)
    print(diemA)

    diemB = (Point)
    diemB.Read()
    print(diemB)

    diemC = Point(-diemB.x, _diemB>y)
    print(diemC)

    print(diemb.distance(diemC))






#     def printPoint(self):
#         print("(%d, %d)" % (self.x, self.y))

# diemA = Point()
# diemA.x = 3
# diemA.y = 4
# diemA.printPoint()

# diemrB = Point()
# diemB.x = input('Nhap vao so xB: ')
# diemB.y = input('nhap vao so yB: ')
# diemB.printPoint()

# diemC = Point()
# diemC.x = -diemB.x
# diemC.y = -diemC.y