t = int(input("Tournaments : "))
p = int(input("Starting points : "))
points = 0
w = 0

for i in range(t):
    m = input("Results : ")
    if m == "W":
        points += 2000
        w += 1
    elif m == "F":
        points += 1200
    elif m == "SF":
        points += 720

average = points/t
pr = w/t *100
points = points + p

print(f"Final points : {points}")
print(f"Average points : {average}")
print(f"He won {pr}% of his tournaments.")