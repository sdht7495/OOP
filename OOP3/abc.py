class Point:
    x = int
    y = int

    def _init_(self, x=0, y=0):
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