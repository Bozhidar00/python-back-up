capacity = 255
n = int(input())
total_liters = 0

for _ in range(n):
    liters = int(input())

    if total_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters

print(total_liters)
