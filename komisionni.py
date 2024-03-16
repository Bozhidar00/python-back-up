g = input("Град : ")
p = float(input("Обем на продажби : "))

if g == "София":
    if 0<= p <= 500:
        c = (p * 5)/100
        print(round(c,2))
    elif 500< p <= 1000:
        c = (p * 7)/100
        print(round(c, 2))
    elif 1000 < p <= 10000:
        c = (p * 8)/100
        print(round(c, 2))
    elif p > 10000:
        c = (p * 12)/100

elif g == "Варна":
    if 0<= p <= 500:
        c = (p * 4.5)/100
        print(round(c,2))
    elif 500< p <= 1000:
        c = (p * 7.5)/100
        print(round(c, 2))
    elif 1000 < p <= 10000:
        c = (p * 10)/100
        print(round(c, 2))
    elif p > 10000:
        c = (p * 13)/100

elif g == "Пловдив":
    if 0<= p <= 500:
        c = (p * 5.5)/100
        print(round(c,2))
    elif 500< p <= 1000:
        c = (p * 8)/100
        print(round(c, 2))
    elif 1000 < p <= 10000:
        c = (p * 12)/100
        print(round(c, 2))
    elif p > 10000:
        c = (p * 14.5)/100

else:
    print("error")