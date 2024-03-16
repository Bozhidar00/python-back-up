h = int(input("Hours : "))
m = int(input("Minutes : ")) + 15
if 0 <= h <= 23:
    pass
if 0 <= m <= 59:
    pass
    print(f"{h}:{m}")
else:
    print("error")