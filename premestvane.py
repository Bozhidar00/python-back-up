w = int(input("Width : "))
l = int(input("Length : "))
h = int(input("Height : "))
s = w * l * h
sum = 0
k = input("Boxes : ")
kn = int(k)
sum += kn
while k != "Done":
    # kn = int(k)
    # sum += kn
    k = input("Boxes : ")
    if sum > s:
        d = sum - s
        print(f"No more free space! You need {d} Cubic meters more.")
        break
    elif s == "Done":
        l = s - sum
        print(f"{l} Cubic meters left.")
        break
kd = sum - c
if s