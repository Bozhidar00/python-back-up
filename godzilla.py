b = float(input("Бюджет : "))
s = int(input("Брой статисти : "))
c = float(input("Цена на облеклото : "))
d = (b * 10) /100
if s > 150:
    c2 = (c * 10) / 100
    c3 = c - c2
    p = s * c3
    total = p + d
    l = b - total
    if l > 0:
        print(f"Ура, филма започва да се снима с {round(l, 2)} останали лева!")
    else:
        print(f"Няма достатъчно пари :( {round(l, 2)} лева не стигат.")
else:
    p2 = s * c
    total2 = p2 + d
    l2 = b - total2
    if l2 > 0:
        print(f"Ура, филма започва да се снима с {round(l2< 2)} останали лева!")
    else:
        print(f"Няма достатъчно пари :( {round(l2, 2)} лева не стигат.")