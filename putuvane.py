b = float(input("Budget : "))
s = input("Season : ")
p = 0

if b <= 100:
    if s == "Summer":
        p = (b * 30)/100
        print(f"Somewhere in Bulgaria. Camp - {round(p, 2)} leva")
    if s == "Winter":
        p = (b * 70)/100
        print(f"Somewhere in Bulgaria. Hotel - {round(p , 2)} leva")

elif b <= 1000:
    if s == "Summer":
        p = (b * 40)/100
        print(f"Somewhere in the Balkans. Camp - {round(p, 2)} leva")
    if s == "Winter":
        p = (b * 80)/100
        print(f"Somewhere in the Balkans. Hotel - {round(p , 2)} leva")

elif b > 1000:
    p = (b*90/100)
    print(f"Somewhere in Europe. Hotel - {round(p , 2)} leva")