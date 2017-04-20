# construcnt a class called circle by radius
# built two methods to calculate area and perimeter of circle

import math

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_of_circle = math.pi * math.pow(self.radius, 2)
        return area_of_circle

    def perimeter(self):
        perimeter_of_circle = 2 * math.pi * self.radius
        return perimeter_of_circle


circle_metrics = Circle(3)
print(circle_metrics.perimeter())
print(circle_metrics.area())


