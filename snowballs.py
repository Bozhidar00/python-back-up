n = int(input())

max_value = float('-inf')

for i in range(n):
    w = int(input())
    t = int(input())
    q = int(input())

    s = w / (t ** q)

    max_value = max(max_value, s)

print(max_value)