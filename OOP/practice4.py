# construct a class calle rectangle by length and width
# and also a method to calculate the area of rectangle

class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_rec = self.length * self.width
        return area_rec


area_of_rectangle = Rectangle(3, 4)
print(area_of_rectangle.area())
