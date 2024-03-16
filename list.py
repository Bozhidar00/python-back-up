n = int(input())
l = []
n2 = int(input())
l2 = []
for i in range(n+1):
    l.append(i)
for i2 in range(n2+1):
    l2.append(i2)
for num in l:
    if num in l2:
        print(num,end=" ")