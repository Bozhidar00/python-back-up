a = input("Actor : ")
p = float(input("Points given from the Academy : "))
n = int(input("Judges :"))
points = 0

for i in range(n):
    o = input("Name of the judge : ")
    pj = float(input("Points given from the judge : "))
    #points += pj
    p = p + ((len(o)*pj)/ 2)

#total = p + pj

if p  > 1250.5:
    print(f"Congratulations, {a} got a nominee for leading role with {p} points!")
else:
    l = 1250.5 - p
    print(f"Sorry, {a}! You need {l} more :(")