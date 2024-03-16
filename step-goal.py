s = float(input("Скорост : "))
if s <= 10:
    print("slow")
if s > 10 and s <= 50:
    print("average")
if s > 50 and s <=150:
    print("fast")
if s > 150 and s <= 1000:
    print("ultra fast")
if s > 1000:
    print("ultra fast")