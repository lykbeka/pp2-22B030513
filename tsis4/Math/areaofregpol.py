import math
sides=int(input())
length=float(input())
def area(sides,length):
    return (sides*math.pow(length,2))/(4*math.tan(math.pi/4))
print(area(sides,length))