f = int(input())
s = int(input())
m = int(input())
count = 0

for i in range(f, s + 1):
    for i2 in range(f, s + 1):
        sum = i + i2
        count += 1
        if sum == m:
            print(f"Combination N:{count} ({i} + {i2} = {m})")
            exit()