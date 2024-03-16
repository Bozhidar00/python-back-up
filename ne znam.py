n = int(input())
l = []
for i in range(n):
    l.append(i)
    if i%2 == 0:
        pass
    else:
        l.remove(i)
print(l)