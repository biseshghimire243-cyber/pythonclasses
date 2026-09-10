import math

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

volume = math.pi * radius ** 2 * height

print("Volume:", round(volume, 2))