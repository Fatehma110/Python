class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
    
    def scale(self, factor):
        self.width *= factor # Same as: self.width = self.width * factor
        self.height *= factor # Same as: self.height = self.height * factor
        print(f"Rectangle scaled by {factor}x. New Dimensions: {self.width} x {self.height}")

    def get_info(self):
        #Return formatted information about the rectangle
        shape_type = "Square" if self.is_square else "Rectangle"
        return f'{shape_type}: {self.width} x {self.height}'
    

#Test code
rectangle1 = Rectangle(8, 30)
print(f"Created: {rectangle1.get_info()}")
print(f"Area: {rectangle1.area()}")
print(f"Perimeter: {rectangle1.perimeter()}")
print(f'Is it Square? {rectangle1.is_square()}')

print("\n" + "="*50)



    