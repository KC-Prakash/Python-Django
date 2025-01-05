import math

def area_of_circle(radius):
    
    if radius< 0:
        raise ValueError("Radius cannot be negative.")
    
    return math.pi * (radius **2)

def area_of_triangle(base, height):
    if base < 0 or height < 0:
        print("Error: Base and height cannot be negative.")
        return None
    return 0.5 * base * height
