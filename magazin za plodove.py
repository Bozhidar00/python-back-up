b = 2.50
a = 1.20
o = 0.85
g = 1.45
k = 2.70
p = 5.50
l = 3.85

b2 = 2.70
a2 = 1.25
o2 = 0.90
g2 = 1.60
k2 = 3.00
p2 = 5.60
l2 = 4.20

f = input("Fruit : ")
d = input("Day of the week : ")
s = float(input("Amount of fruit : "))

if f == "Banana":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c = b*s
        print(f"Your bananas will cost {round(c,2)} leva.")
    elif d == "Sunday" or "Saturday":
        c2 = b2*s
        print(f"Your bananas will cost {round(c2,2)} leva.")

elif f == "Apple":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c3 = a*s
        print(f"Your apples will cost {round(c3, 2)} leva.")
    elif d == "Sunday" or "Saturday":
        c4 = a2 * s
        print(f"Your apples will cost {round(c4, 2)} leva.")

elif f == "Orange":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c5 = o * s
        print(f"Your oranges will cost {round(c5, 2)} leva.")
    elif d in ["Sunday", "Saturday"]:
        c6 = o2 * s
        print("Your oranges will cost {:.2f} leva.".format(c6))
elif f == "Grapefruit":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c7 = g * s
        print(f"Your grapefruit will cost {round(c7, 2)} leva.")
    elif d == "Sunday" or "Saturday":
        c8 = g2 * s
        print(f"Your grapefruit will cost {round(c8, 2)} leva.")

elif f == "Kiwi":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c9 = k * s
        print(f"Your kiwis will cost {round(c9, 2)} leva.")
    elif d == "Sunday" or "Saturday":
        c10 = k2 * s
        print(f"Your kiwis will cost {round(c10, 2)} leva.")

elif f == "Pienapple":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c11 = p * s
        print(f"Your pienapples will cost {round(c11, 2)} leva.")
    elif d == "Sunday" or "Saturday":
        c12 = p2 * s
        print(f"Your pienapples will cost {round(c12, 2)} leva.")

elif f == "Grapes":
    if d == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        c13 = l * s
        print(f"Your grapes will cost {round(c13, 2)} leva.")
    elif d == "Sunday" or "Saturday":
        c14 = l2 * s
        print(f"Your grapes will cost {round(c14, 2)} leva.")
else:
    print("error")