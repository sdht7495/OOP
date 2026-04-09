import math 

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

class HinhChuNhat:
    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner
        self.width = width
        self.height = height

class HinhTron:
    def __init__(self, center: Point, radius: float):
        self.center = center 
        self.radius = radius

def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def DiemTrongHinhTron(tron: HinhTron, point: Point) -> bool:
    return distance(tron.center, point) <= tron.radius

def NamHoanToanTrongHinhTron(tron: HinhTron, CN: HinhChuNhat) -> bool:
    c = CN.corner
    corners = [
        Point(c.x, c.y),
        Point(c.x + CN.width, c.y),
        Point(c.x, c.y + CN.height),
        Point(c.x + CN.width, c.y + CN.height),
    ]
    return all(DiemTrongHinhTron(tron, p)for p in corners)


def CNTron(tron: HinhTron, CN: HinhChuNhat) -> bool:
    closest_x = max(CN.corner.x, min(tron.center.x, CN.corner.x + CN.width))
    closest_y = max(CN.corner.y, min(tron.center.y, CN.corner.y + CN.height))
    closest_point = Point(closest_x, closest_y)
    return DiemTrongHinhTron(tron, closest_point)
