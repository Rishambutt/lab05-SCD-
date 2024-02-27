# Importing the classes from shapes.py
from shapes import Rectangle, Circle

# Function to print details of a Shape object
def print_details(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Instantiating objects of Rectangle and Circle
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Demonstrating polymorphism by calling print_details with instances of both Rectangle and Circle
print("Details for Rectangle:")
print_details(rectangle)

print("\nDetails for Circle:")
print_details(circle)
