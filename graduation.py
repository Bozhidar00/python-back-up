n = input("Name : ")
count = 1
mark = 0
p = 0

for i in range(12):
    m = float(input("Mark : "))
    if 6>= m >= 4:
        count += 1
        mark += m
        p += 1
        pass
    else:
        print(f"{n} has been excluded in the {count} grade.")
        break
if p == 12:
    a = mark / 12
    print(f"{n} graduated! Average mark : {round(a, 2)}")