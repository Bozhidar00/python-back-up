p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

n = int(input("Input number : "))

for i in range(n):
    m = int(input())

if m < 200:
    n1 += 1

elif 200<=m<=399:
    n2 += 1

elif 400<=m<=599:
    n3 += 1

elif 600<=m<799:
    n4 += 1

else:
    n5 += 1

p1 = n1/n * 100
p2 = n2/n * 100
p3 = n3/n * 100
p4 = n4/n * 100
p5 = n5/n * 100

print(f"{round(p1, 2)}%")
print(f"{round(p2, 2)}%")
print(f"{round(p3, 2)}%")
print(f"{round(p4, 2)}%")
print(f"{round(p5, 2)}%")