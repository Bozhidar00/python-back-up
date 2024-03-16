d = input("Destination : ")
b = float(input("Budget : "))
total = 0

while d != "End":
    e = float(input("Earnings : "))
    total += e
    if total >= b:
        print(f"Going to {d}")
        d = input("Destination : ")
        if d == "End":
            break
        else :
            pass
        b = float(input("Budget : "))
        e = float(input("Earnings : "))
        total += e
        ib = int(b)