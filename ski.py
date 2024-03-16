r = 18
a = 25
p = 35

s = int(input("Length of stay : "))
t = input("Room, Apartment or President apartment ")
re = input("Review : ")

if t == "Apartment":
    if s < 10:
        pr = a * (s - 1)
        d = pr*30 / 100
        pr = pr - d

    elif 15 >= s == 10:
        pr = a * (s - 1)
        d = pr*35 / 100
        pr = pr - d

    elif s > 15:
        pr3 = a * (s - 1)
        d = pr3*50 / 100
        pr3 = pr3 - d

elif t == "President Apartment":
    if s < 10:
        pr4 = (s - 1) * p
        d = pr4*10 / 100
        pr4 = pr4 - d

    elif 15 >= s == 10:
        pr5 = (s - 1) * p
        d = pr5 * 15 / 100
        pr5 = pr5 - d

    elif s > 15:
        pr6 = (s - 1) * p
        d = pr6 * 20 / 100
        pr6 = pr6 - d


elif t == "Room":
    # pr7 = r * (s - 1)


 if re == "positive":
    l = pr * 25 / 100
    pr = pr + l
elif re == "negative":
    l1 = pr * 10 / 100
    pr = pr - l1

print(round(pr, 2))