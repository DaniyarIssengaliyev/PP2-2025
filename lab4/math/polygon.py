import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

print("The area of the polygon is:", round((sides * pow(length,2))/ 4 * math.tan(math.pi/sides)))