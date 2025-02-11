class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculateArea(self):
        area = self.width * self.height 
        print(f"Area of the rectangle is: {area: .2f}")
        

rectangle = Rectangle(2, 5).calculateArea()
    