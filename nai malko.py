n = input()
while n != "stop":
    cn = float(n)
    n = input()
    if n == "stop":
        list = [cn]
        minValue = min(list)
        print(minValue)