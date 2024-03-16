w = input("Word : ")
l = []
l2 = []
l3 = []
l.append(w)
while w != "stop":
    w = input("Word : ")
    l.append(w)
    if w == "stop":
        l.remove(w)
        break

for word in l:
    wl = len(word)
    if wl == 2:
        l2.append(word)
        print(l2)
    elif wl == 3:
        l3.append(word)
        print(l3)