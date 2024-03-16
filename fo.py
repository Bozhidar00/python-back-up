n = int(input())
count = 0
for i in range(0,n):
    m = int(input())
    count += 1
    if count%2 == 0:
        sum = m + m
    else:
        sum2 = m + m
if sum == sum2:
    print(f"yes sum = {sum}")
elif sum > sum2:
    d = sum - sum2
    print(f"no diff = {d}")
elif sum2 > sum:
    d = sum2 - sum
    print(f"no, diff = {d}")