f = input("Fruit : ")
d = input("Day of the week :")
s = float(input("Amount of fruit : "))
price = 0

if d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if f  == "banana":
        price = 2.50
    elif f == "apple":
        price = 1.20
    elif f == "orange":
        price = 0.85
    elif f == "grapefruit":
        price = 1.45
    elif f == "kiwi":
        price = 2.70
    elif f == "pienapple":
        price = 5.50
    elif f == "grapes":
        price = 3.85
    else:
        print("error")
        exit()
    print("{:.2f}".format(price * s))
elif d in ["Saturday", "Sunday"]:
    if f  == "banana":
        price = 2.70
    elif f == "apple":
        price = 1.25
    elif f == "orange":
        price = 0.90
    elif f == "grapefruit":
        price = 1.60
    elif f == "kiwi":
        price = 3.00
    elif f == "pienapple":
        price = 5.60
    elif f == "grapes":
        price = 4.20
    else:
        print("error")
        exit()
    print("{:.2f}".format(price*s))
else:
    print("error")