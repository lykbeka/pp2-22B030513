import math
h=int(input())
a=int(input())
b=int(input())
base=[a,b]
def area(base, h):
    return math.fsum(base)*h/2
print(area(base, h))