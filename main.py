#quadratic formula algorithm

import math


a = int(input("what is your a variable? "))

b = int(input("what is your b variable? "))

c = int(input("what is your c variable? "))

while c >= 0:
    c = int(input("c must be a negative "))

x1 = (((-b)+(math.sqrt((b**2)-(4*a*c))))/(2*a))

x2 = (((-b)-(math.sqrt((b**2)-(4*a*c))))/(2*a))

print(f"x1 = {x1}, x2 = {x2}")


