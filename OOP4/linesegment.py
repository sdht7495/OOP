import math
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(4, 6)
            self.__d2 = Point(7, 13)

        elif len(args) == 2 and isinstance(args[0], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        
        elif en(args) == 1 and isinstance(args[0], LineSegment):
            src = args[0]
            self.__d1 = Point(src.getD1().x, src.getD1().y)
            self.__d2 = Point(src.getD2().x, src.getD2().y)

        else:
            raise ValueError("tham so khong hop le")
        
    def getD1(self):
        return self.__d1
    
    def getD2(self):
        return self.__d2
    
    def setD1(self):
        self.__d1 = d1

    def setD2(self):
        self.__d2 = d2

    def length(self):
        dx = self.__d1.x - self.__d2.x
        dy = self.__d1.y - self.__d2.y
        return math.sqrt(dx**2 + dy**2)
    
    def hienThi(self):
        print(f"LineSegment[{self.__d1} -> {self.__d2}]")

