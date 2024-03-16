m = input("Month : ")
n = int(input("Length of stay : "))

if m == "May" or m == "October":
    s = 50
    a = 65
    ps = n * s
    pa = n * a
    if n > 7:
        ds = (s * 5)/100
        s = s - ds
        ps = n * s
    elif n > 14:
        ds = (s * 30) / 100
        s = s - ds
        ps = n * s
        da = (a * 10) / 100
        a = a - da
        pa = n * a
    print(f"Apartment : {round(pa , 2)}lv."
          f"Studio : {round(ps , 2)}lv.")

elif m == "June" or m == "September":
    s = 75.20
    a = 68.70
    ps = n * s
    pa = n * a
    if n > 14:
        ds = (s * 20) / 100
        s = s - ds
        ps = n * s
        da = (a * 10) / 100
        a = a - da
        pa = n * a
    print(f"Apartment : {round(pa, 2)}lv."
          f"Studio : {round(ps, 2)}lv.")

elif m == "July" or m == "August":
    s = 76
    a = 77
    ps = n * s
    pa = n * a
    if n > 14:
        da = (a * 10) / 100
        a = a - da
        pa = n * a
    print(f"Apartment : {round(pa, 2)}lv."
          f"Studio : {round(ps, 2)}lv.")