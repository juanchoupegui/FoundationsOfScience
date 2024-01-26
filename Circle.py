import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = self.radius * self.radius * math.pi
        return area
