y1 = 0
x1 = 0
y2 = 0
x2 = 0

coordinates = input("enter your first pair of coordinates with a comma separating each point. ")

splitcoordinate1 = coordinates.split(", ", 1)

x1 = int(splitcoordinate1[0])
y1 = int(splitcoordinate1[1])

coordinates = input("enter your second pair of coordinates with a comma separating each point. ")

splitcoordinate2 = coordinates.split(", ", 1)

x2 = int(splitcoordinate2[0])
y2 = int(splitcoordinate2[1])

m = (y2 - y1)/(x2 - x1)
c = m*(-x1) + y1
print(f"y = {m}x + {c}")