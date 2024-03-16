b = float(input("Бюджет : "))
n = int(input("Брой видеокарти : "))
m = int(input("Брой процесори : "))
p = int(input("Брой рам памет : "))

v = 250
n2 = n*v
m2 = (n2*35)/100
m3 = m * m2
p2 = (n2*10)/100
p3 = p * p2

total = m3 + p3 + n2

if n > m:
    total = total - ((total*15)/100)

if b > total:
    l = b - total
    print(f"Остават {round(l, 2)} лева бюджет!")
else:
    l2 = total - b
    print(f"Бюджетът не стига с {round(l2, 2)} лева.")