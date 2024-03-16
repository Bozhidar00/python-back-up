import sys
n =int(input())
for i in range(n):
    m = str(input())
max = -sys.maxsize
if m > max:
    m = max
    print(f"Max number is {m}.")
min = -sys.minimize
if m < min:
    m = min
    print(f"Min numver is {m}.")