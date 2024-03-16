a = int(input("Age :"))
g = input("m or f : ")
if g == "m" or "f":
    pass
else:
    print("error")
if g == "m":
    if a >= 16:
        print("Mr.")
    else:
        print("Master")
if g == "f":
    if a >= 16:
        print("Ms.")
    else:
        print("Miss")