p = 2.60
d = 3
t = 4.10
m = 8.20
tr = 2

trip = float(input("Цена на екскурзията : "))

p2 = int(input("Брой пъзели : "))
d2 = int(input("Брой кукли : "))
t2 = int(input("Брой мечета : "))
m2 = int(input("Брой миниони : "))
tr2 = int(input("Брой камиончета : "))
total = p2 + d2 + t2 + m2 + tr2

p3 = p2 * p
d3 = d2 * d
t3 = t2 * t
m3 = m2 * m
tr3 = tr2 * tr
total2 = p3 + d3 + t3 + m3 + tr3

if total >= 50:
    total3 = (total * 25) / 100
    r = (total3 * 10) / 100
    total4 = total3 - r
    if total4 >= trip:
        c = total4 - trip
        print(f"Ще има екскурзия! {round(c, 2)} лева остават.")
    else:
        n = trip - total4
        print(f"Няма да има екскурзия :(. {round(n, 2)} лева не стигат.")
else:
    r2 = (total2 * 10)/100
    total5 = total2 - r2
    if total5 >= trip:
        c2 = total5 - trip
        print(f"Ще има екскурзия! {round(c2, 2)} лева остават.")
    else:
        n2 = trip - total5
        print(f"Няма да има екскурзия :(. {round(n2, 2)} лева не стигат.")