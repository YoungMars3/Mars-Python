class Shape:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"I am a {self.name}"

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

#Creating instances
rectangle = Rectangle("Rectangle", 5, 10)
circle = Circle("Circle", 7)

#Accessing methods
print(rectangle.info()) #Output: I am a rectangle
print(rectangle.area()) #Output: 50
print(circle.info())    #Output: I am a circle
print(circle.area())    #Output: 153.86 (approximately)