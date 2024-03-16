s = input("Steps : ")
s1 = int(s)
total = 0
total += s1

while s != "Going Home":
    sn = int(s)
    s = input("Steps : ")
    total += sn
    if s == "Going Home":
        sl = ("Steps while walking home : ")
        sl1 = int(sl)
        total += sl1
    elif total >= 10000:
        l = total - 10000
        print(f"Goal reached! {l} steps over the goal!")
        break
if total < 10000:
    d = 10000 - total
    print(f"{d} more steps to reach the goal.")
