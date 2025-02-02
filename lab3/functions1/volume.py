import math
def volume():
    return 4/3 * math.pi * radius**3

radius = int(input("Enter radius of a sphere: "))
print(volume())