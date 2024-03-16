r = 5
d = 3.80
l = 2.80
na = 3
g = 2.50

f = input("Flowers : (Roses, Dahlias, Tulips, Narcissus, Gladiolus)")
n = int(input("Amount of flowers : "))
b = int(input("Budget : "))

if f == "Roses":
    pr = n * r
    if n > 80:
        d = (pr*10)/100
        pr = pr - d
    if pr <= b:
        l = b - pr
        print(f"Neli wants {n} {f}. The price of a single rose is 5 leva, and she will need {pr} leva. After paying she will have {l} leva left.")
    else:
        m = pr - b
        print(f"Neli wants {n} {f}. The price of a single rose is 5 leva, and she will need {pr} leva. However, her budget is too low, she needs another {m} leva.")

elif f == "Dahlias":
    pr2 = n * d
    if n > 90:
        d2 = (d * 15)/100
        pr2 = pr2 - d2
    if pr2 <= b:
        l2 = b - pr2
        print(f"Neli wants {n} {f}. The price of a single dahlia is 3.80 leva, and she will need {pr2} leva. After paying she will have {l2} leva left.")
    else:
        m2 = pr2 - b
        print(f"Neli wants {n} {f}. The price of a dahlia is 3.80 leva, and she will need {pr2} leva. However, her budget is too low, she needs another {m2} leva.")

elif f == "Tulips":
    pr3 = n * t
    if n > 80:
        d3 = (t * 15)/100
        pr3 = pr3 - d
    if pr3 <= b:
        l3 = b - pr3
        print(f"Neli wants {n} {f}. The price of a single tulip is 2.80 leva, and she will need {pr3} leva. After paying she will have {l3} leva left.")
    else:
        m3 = pr3 - b
        print(f"Neli wants {n} {f}. The price of a tulip is 2.80 leva, and she will need {pr3} leva. However, her budget is too low, she needs another {m3} leva.")

elif f == "Narcissus":
    pr4 = n * nr
    if n < 120:
        i = (pr4 * 15)/100
        pr4 = pr4 + i
    if pr4 <= b:
        l4 = b - pr4
        print(f"Neli wants {n} {f}. The price of a single narcissus is 3 leva, and she will need {pr4} leva. After paying she will have {l4} leva left.")
    else:
        m4 = pr4 - b
        print(f"Neli wants {n} {f}. The price of a narcissus is 3 leva, and she will need {pr4} leva. However, her budget is too low, she needs another {m4} leva.")

elif f == "Gladiolus":
    pr5 = n * g
    if n < 80:
        i5 = (pr5 * 20)/100
        pr5 = pr5 + i5
    if pr5 <= b:
        l5 = b - pr5
        print(f"Neli wants {n} {f}. The price of a single gladiolus is 2.50 leva, and she will need {pr5} leva. After paying she will have {l5} leva left.")
    else:
        m5 = pr5 - b
        print(f"Neli wants {n} {f}. The price of a gladiolus is 2.50 leva, and she will need {pr5} leva. However, her budget is too low, she needs another {m5} leva.")