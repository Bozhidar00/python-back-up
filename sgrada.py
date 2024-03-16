f = int(input("Floors : "))
r = int(input("Rooms : "))

o = r
a = r
l = r
nl = 0
no = 0
na = 0

for i in range(f):
    if i%2 == 0:
        o += 1
    else:
        a += 1

if f%2 == 0:
    o -= 1
else:
    a -= 1

for i in range(0,l):
    print(f"L{f}{nl}")
    nl += 1

if (f - 1)%2 == 0:
    while f > 0:
        f -= 1
        for i in range(0 , r):
            print(f"O{f}{no}")
            no += 1
        f -= 1
        no = 0
        for i in range(0 , r):
            print(f"A{f}{na}")
            na += 1
        f -= 1
        na = 0

elif (f - 1)%2 != 0:
    while f > 0:
        f -= 1
        for i in range(0 , r):
            print(f"A{f}{na}")
            na += 1
        f -= 1
        na = 0
        for i in range(0 , r):
            print(f"O{f}{no}")
            no += 1
        f -= 1
        no = 0