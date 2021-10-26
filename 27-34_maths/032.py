import math

radius = float(input("Enter the radius of a cylinder: "))
depth = float(input("Enter the depth of a cylinder: "))

circle_area = math.pi * (radius**2)
volume = circle_area * depth

print(round(volume, 3))