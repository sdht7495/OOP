from abc import Point
import copy

class linesegment:
    def __init__(self,*args):
        if len(args)==0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        if len(args)==2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]

        if len(args)==4:
            if isinstance(args[0], int):
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3])

        if len(args)==1:
            if isinstance(args[0], linesegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)

    def __str__(self):
        return "[(%d, %d), (%d, %d)]" % \
            (self.__d1.x, self.__d1.y, self.__d2.x, self.__d2.y)
    
    def getD1(self):
        return self.__d1
    
    def getD2(self):
        return self.__d2
    
    def setD1D2(self, p1, p2):
        self.__d1 = p1
        self.__d2 = p2

if __name__ == "__main__":
    
    l1 = linesegment
    print(l1)

    p1 = Point(3, 4)
    p2 = Point(5, 6)
    l2 = linesegment(p1,p2)
    print(l2)

    l3 = linesegment(3, 6, 7, 8)
    print(l3)

    l4 = linesegment(l1)
    print(l4)

    print(l4.getD1())
    print(l4.getD2())

    l4.setD1D2(Point(-3, -5), Point(10, 20))
    print(l4)