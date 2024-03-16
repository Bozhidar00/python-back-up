f = 150
i = 100
r = 50

ft = 0
it = 0
rt = 0

t = int(input("Open tabs : "))
s = float(input("Salary : "))

for i in range(t):
    n = input()

    if n == "Facebook":
        ft += 1
    elif n == "Instagram":
        it += 1
    elif n == "Reddit":
        rt += 1

f1 = f * ft
i1 = i * it
r1 = r * rt
sum = f1 + i1 + r1
s = s - sum

if s <= 0:
    print("You have lost your salary :(")
else:
    print(f"You have {round(s, 2)} leva left.")