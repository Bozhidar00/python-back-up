import math
s = str(input("Choose shape [square, rectangle, circle, triangle]"))
if s == "square":
    l = float(input("Enter length of the sides : "))
    area = l*l
    print(str(area)[:7])
elif s == "rectangle":
    a = float("Enter length of a : ")
    b = float("Enter length of b : ")
    area2 = a*b
    print(str(area2)[:7])
elif s == "triangle":
    c = float(input("Enther length of the hypotenuse : "))
    h = float(input("Enther the length of the altitude to the hypotenuse : "))
    area3 = (c*h)/2
    print(str(area3)[:7])
elif s == "circle":
    r = float(input("Enther length of the circle : "))
    area4 = math.pi*(r*r)
    print(str(area4)[:7])
else:
    print("Error :(")