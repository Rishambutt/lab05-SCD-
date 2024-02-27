class Shape:
    def area(self):
        pass  # Placeholder method for calculating the area of a shape
    
    def perimeter(self):
        pass  # Placeholder method for calculating the perimeter of a shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width  # Initialize width
        self.__height = height  # Initialize height
    
    def get_width(self):
        return self.__width  # Getter method for width
    
    def set_width(self, width):
        self.__width = width  # Setter method for width
    
    def get_height(self):
        return self.__height  # Getter method for height
    
    def set_height(self, height):
        self.__height = height  # Setter method for height
    
    def area(self):
        return self.__width * self.__height  # Calculate area of rectangle
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)  # Calculate perimeter of rectangle

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # Initialize radius
    
    def get_radius(self):
        return self.__radius  # Getter method for radius
    
    def set_radius(self, radius):
        self.__radius = radius  # Setter method for radius
    
    def area(self):
        import math
        return math.pi * self.__radius ** 2  # Calculate area of circle using pi*r^2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.__radius  # Calculate perimeter of circle using 2*pi*r

# Creating instances of Rectangle and Circle
rectangle = Rectangle(5, 4)
print(" Draw for Rectangle:")
print("Area:", rectangle.area())  # Print area of rectangle
print("Perimeter:", rectangle.perimeter())  # Print perimeter of rectangle

circle = Circle(3)
print("Draw for circle:")
print("Area:", circle.area())  # Print area of circle
print("Perimeter:", circle.perimeter())  # Print perimeter of circle

