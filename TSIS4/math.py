import math

def degree_to_radian(deg):
    return deg * (math.pi / 180)

deg = float(input("Input degree: "))
print(f"Output radian: {degree_to_radian(deg):.6f}")

def trapezoid_area(h, a, b):
    return 0.5 * (a + b) * h

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
print(f"Expected Output: {trapezoid_area(h, a, b)}")

def polygon_area(sides, length):
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
print(f"The area of the polygon is: {polygon_area(sides, length):.6f}")

def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
print(f"Expected Output: {parallelogram_area(base, height)}")
