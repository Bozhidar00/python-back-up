a = int(input("Age : "))
p = float(input("Price of the washing machine : "))
t = int(input("Price of the toy : "))
savings = 0
sum = 0
toys = 0

for i in range(1, a + 1):
    if i%2 == 0:
        savings += (sum - 1)
        sum += 10
    else:
        toys += 1
        savings += (toys*t)

if savings >= p:
    l = savings - p
    print(f"Yay! She can buy the washing machine with {round(l, 2)} leva left!")
else:
    n = p - savings
    print(f"Lily cannot buy the washing machine. She needs {round(n, 2)} leva.")