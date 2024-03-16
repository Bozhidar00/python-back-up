n1 = int(input("First number : "))
n2 = int(input("Second number : "))
o = input("Operation : ")

if o == "+":
    r = n1 + n2
    if (r % 2) == 0:
        print(f"{n1} {o} {n2} = {r} - even")
    else:
        print(f"{n1} {o} {n2} = {r} - odd")

elif o == "-":
    r = n1 - n2
    if (r % 2) == 0:
        print(f"{n1} {o} {n2} = {r} - even")
    else:
        print(f"{n1} {o} {n2} = {r} - odd")

elif o == "*":
    r = n1 * n2
    if (r % 2) == 0:
        print(f"{n1} {o} {n2} = {r} - even")
    else:
        print(f"{n1} {o} {n2} = {r} - odd")

elif o == "/":
    r = n1 / n2
    print(f"{n1} {o} {n2} = {round(r , 2)}")
    if n2 == 0:
        print(f"Cannot divide {n1} by 0.")

elif o == "%":
    r = n1 % n2
    print(f"{n1} {o} {n2} = {r}")
    if n2 == 0:
        print(f"Cannot divide {n1} by 0.")