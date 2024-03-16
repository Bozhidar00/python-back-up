n = input()
while n != "stop":
    cn = float(n)
    n = input()
    if n == "stop":
        list = [cn]
        maxValue = max(list)
        print(maxValue)