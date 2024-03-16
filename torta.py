w = int(input("Width : "))
l = int(input("Length : "))
s = w * l #broi parcheta
c = 0  #pak broi parcheta?
while s > c:
    p = input("Cake : ")  #kolko parcheta sa vzeli
    if p == "STOP":
        break
    ps = int(p)
    c += ps    #kolko parcheta ostavat
pd = abs(s - c)
if s > c:
    print(f"{pd} pieces are left.")
else:
    print(f"No more cake left! You need {pd} pieces more.")