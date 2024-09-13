from math import pi

def circle_area(r):
    return pi*(r**2)

def triangle_area(h):
    return 0.5*h

def perimeter(a,b):
    return (a+b)*2

def rectangle_area(a,b):
    return a*b

print(circle_area(3))
print(rectangle_area(5, 7))
print(triangle_area(6))
print(perimeter(10, 5))