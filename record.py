r = float(input("Рекордът (в секунди) : "))
m = float(input("Разстоянието (в метри) : "))
t = float(input("Времето, в секунди, за което плува разстояние от 1 метър : "))
time = m * t
if m > 14:
    s = (m/15)*12.5
    total = time + s
else:
    total = time
if total > r:
    print(f"Иван не успя да бие рекорда :(")
else:
    print(f"Ура, Иван успя да бие рекорда! Новият рекод е {total}!")