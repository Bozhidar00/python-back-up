ps = 3000
pa = 4200
pw = 2600

b = float(input("Their budget is : "))
s = input("The season is: ")
r = int(input("Number of fishermen : "))

if s == "Spring":
    if r <= 6:
        d = (ps*10)/100
        p = ps - d
    elif r >= 7 and r <= 11:
        d = (ps*15)/100
        p = ps - d
    elif r >= 12:
        d = (ps*25)/100
        p = ps - d
    if (r % 2) == 0:
        d2 = (p * 5)/100
        p = p - d2
    if b >= p:
        l = b - p
        print(f"Yay! You have enough money to go on a fishing trip! You have {round(l, 2)} money left!")
    else:
        l2 = p - b
        print(f"You do not have enough money :(. You will need {round(l2, 2)} more")

if s == "Summer":
    if r <= 6:
        d = (pa*10)/100
        p = pa - d
    elif r >= 7 and r <= 11:
        d = (pa*15)/100
        p = pa - d
    elif r >= 12:
        d = (pa*25)/100
        p = pa - d
    if (r % 2) == 0:
        d2 = (p * 5)/100
        p = p - d2
    else:
        pass
    if b >= p:
        l = b - p
        print(f"Yay! You have enough money to go on a fishing trip! You have {round(l, 2)} money left!")
    else:
        l2 = p - b
        print(f"You do not have enough money :(. You will need {round(l2, 2)} more")

if s == "Autumn":
    if r <= 6:
        d = (pa*10)/100
        p = pa - d
    elif r >= 7 and r <= 11:
        d = (pa*15)/100
        p = pa - d
    elif r >= 12:
        d = (pa*25)/100
        p = pa - d
    if b >= p:
        l = b - p
        print(f"Yay! You have enough money to go on a fishing trip! You have {round(l, 2)} money left!")
    else:
        l2 = p - b
        print(f"You do not have enough money :(. You will need {round(l2, 2)} more")

if s == "Winter":
    if r <= 6:
        d = (pw*10)/100
        p = pw - d
    elif r >= 7 and r <= 11:
        d = (pw*15)/100
        p = pw - d
    elif r >= 12:
        d = (pw*25)/100
        p = pw - d
    if (r % 2) == 0:
        d2 = (p * 5)/100
        p = p - d2
    if b >= p:
        l = b - p
        print(f"Yay! You have enough money to go on a fishing trip! You have {round(l, 2)} money left!")
    else:
        l2 = p - b
        print(f"You do not have enough money :(. You will need {round(l2, 2)} more")