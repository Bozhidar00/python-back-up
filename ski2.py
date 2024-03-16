r = 18
a = 25
p = 35

s = int(input("Length of stay : "))
t = input("Room, Apartment or President apartment ")
re = input("Review : ")

if t == "Apartment":
    if s < 10:
        pa1 = (s - 1) * a
        d = pa1*30 / 100
        pa1 = pa1 - d
        if re == "positive":
            l = pa1 * 25 / 100
            pa1 = pa1 + l
        elif re == "negative":
            l1 = pa1*10 / 100
            pa1 = pa1 - l1
        print(round(pa1 , 2))

    elif 15 >= s == 10:
        pa = (s - 1) * a
        d = pa*35 / 100
        pa = pa - d
        if re == "positive":
            l = pa * 25 / 100
            pa = pa + l
        elif re == "negative":
            l1 = pa*10 / 100
            pa = pa - l1
        print(round(pa , 2))

    elif 15 > s:
        pa2 = (s - 1)* a
        d = pa2*50 / 100
        pa2 = pa2 - d
        if re == "positive":
            l = pa2 * 25 / 100
            pa2 = pa2 + l
        elif re == "negative":
            l1 = pa2*10 / 100
            pa2 = pa2 - l1
        print(round(pa2 , 2))

elif t == "President Apartment":
    if s < 10:
        ppr = (s - 1) * p
        d = ppr*10 / 100
        ppr = ppr - d
        if re == "positive":
            l = ppr * 25 / 100
            ppr = ppr + l
        elif re == "negative":
            l1 = ppr * 10 / 100
            ppr = ppr - l1
        print(round(ppr, 2))

    elif 15 >= s == 10:
        pp = (s - 1) * p
        d = pp * 20 / 100
        pp = pp - d
        if re == "positive":
            l = pp * 25 / 100
            pp = pp + l
        elif re == "negative":
            l1 = pp * 10 / 100
            pp = pp - l1
        print(round(pp, 2))

    elif 15 > s:
        ppr2 = (s - 1) * p
        d = ppr2 * 10 / 100
        ppr2= ppr2 - d
        if re == "positive":
            l = ppr2 * 25 / 100
            ppr2 = ppr2 + l
        elif re == "negative":
            l1 = ppr2 * 10 / 100
            ppr2 = ppr2 - l1
        print(round(ppr2, 2))

elif t == "Room":
    prr = (s - 1)*r
    if re == "positive":
        l = prr * 25 / 100
        prr = prr + l
    elif re == "negative":
        l1 = prr * 10 / 100
        prr = prr - l1
    print(round(prr, 2))