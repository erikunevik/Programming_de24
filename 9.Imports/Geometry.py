
import math

def area_of_circle(radius):
 
    area = math.pi * math.pow(radius, 2)
    return area

def perimeter_ofcircle(radius):

    permiter = 2 * math.pi * radius

    return permiter



print(area_of_circle(100))

print(perimeter_ofcircle(100))