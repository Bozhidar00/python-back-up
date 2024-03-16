g = int(input("Groups : "))
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for i in range(g):
    c = int(input("Climbers : "))

    if 0 < c <= 5:
        g1 += c
    elif 12 >= c >= 6:
        g2 += c
    elif 25 >= c >= 13:
        g3 += c
    elif 40 >= c >= 26:
        g4 += c
    else:
        g5 += c

total = g1 + g2 + g3 +g4 + g5

pr1 = g1/total * 100
pr2 = g2/total * 100
pr3 = g3/total * 100
pr4 = g4/total * 100
pr5 = g5/total * 100

print(f"Musala - {round(pr1, 2)}%")
print(f"Monblan - {round(pr2, 2)}%")
print(f"Kilimandjaro - {round(pr3 , 2)}%")
print(f"K2 - {round(pr4, 2)}%")
print(f"Everest - {round(pr5, 2)}%")