n = input("Име на сериал : ")
e = int(input("Продължителност на епизод : "))
p = int(input("Продължителност на почивката : "))
t = p * 1/8  #vreme za obqd
o = p * 1/4  #vreme za otdih
l = p - t - o  #ostanalo vreme
if l >= e:
    if l > 0:
        r = l - e
        print(F"Има достатъчно време да изгледаш епозод от {n} , с оставащо време {r}.")
elif l < e:
    r2 = e - l
    print(f"Няма достатъчно време да изгледаш {n}. Трябват ти още {r2} минути.")