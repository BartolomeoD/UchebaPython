import math

radiusInner = int(input("Radius inner = "))
radiusOuter = int(input("Radius outer = "))

innerCircleSquare = math.pi * radiusInner * 2
outerCircleSquare = math.pi * radiusOuter * 2
ringSquare = outerCircleSquare - innerCircleSquare

print("inner = " + str(innerCircleSquare))
print("outer = " + str(outerCircleSquare))
print("ring = " + str(ringSquare))
