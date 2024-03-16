m = 0
i = input("Increase : ")
while i != "NoMoreMoney":
    cs = float(i)
    m +=  cs
    print(f"Increase : {cs:.2f}")
    i = input("Increase : ")
    if i == "NoMoreMoney":
        print("No More Money")
        print(f"Total : {m:.2f}")
        break
    if cs < 0:
        print("Invalid operation!")
        print(f"Total : {cs:.2}")