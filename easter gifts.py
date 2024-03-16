gifts = input().split()
gift_dict = {gift: 1 for gift in gifts}

while True:
    command = input()
    if command == "No Money":
        break

    action, *args = command.split()

    if action == "OutOfStock":
        gift = args[0]
        if gift in gift_dict:
            gift_dict[gift] = None
    elif action == "Required":
        gift, index = args
        index = int(index)
        if 0 <= index < len(gifts):
            gift_dict[gifts[index]] = None
            gifts[index] = gift
    elif action == "JustInCase":
        gift = args[0]
        gifts[-1] = gift

print(" ".join([gift for gift in gifts if gift != "None"]))
