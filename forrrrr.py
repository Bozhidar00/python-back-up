n = int(input())
n1 = int(input())
m = int(input())
m1 = int(input())

sum1 = n + n1
sum2 = m + m1

if sum1 == sum2:
    print(f"Yes, sum = {sum1}.")
elif sum1 < sum2:
    d = sum2 - sum1
    print(f"No, diff = {d}")
elif sum2 < sum1:
    d = sum1 - sum2
    print(f"No, diff = {d}.")