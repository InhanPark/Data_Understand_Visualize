#Define a class Rectangle with attributes width and height,
#and methods to calculate the area and perimeter.

class Rectangle:
    """Rectangle area and parameter calculation"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Rectangle area calculation"""
        # Your code here
        return self.width * self.height
    
    def perimeter(self):
        """Rectangle parameter calculation"""
        # Your code here
        return (self.width * 2) + (self.height * 2)

if __name__ == '__main__':
    rect = Rectangle(4, 5)
    print(rect.area())       # Output: 20
    print(rect.perimeter())  # Output: 18
