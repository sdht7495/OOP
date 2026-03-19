from abc import Point
import math
class Circle:
    center = int
    radius = float

    def _init_(self, center = 0, radius = 0):
        self.center = center
        self.radius = radius