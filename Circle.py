import math

class Circle:

    def __init__(self, radius):
        self.pi = math.pi
        self.radius = radius
    
    def calculateArea(self):
        area = self.pi * (self.radius ** 2) 
        # area = math.pi * (self.radius ** 2) 
        print(f"Area of the circle is: {area: .2f}")
        

circle = Circle(5).calculateArea()
    