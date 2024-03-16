w = int(input("Width : "))
l = int(input("Length : "))
h = int(input("Height : "))
s = w * l * h
sum = 0
while s > sum:
    k = input("Boxes : ")
    if k == "Done":
        break
    kn = int(k)
    sum += kn
kd = sum - s
kl = s - sum
if sum > s:
    print(f"No more free space left. You need {kd} meters more.")
else:
    print(f"{kl} meters left.")