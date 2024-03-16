sh = int(input("Hour of the exam : "))
m = int(input("Minute of the exam : "))
h2 = int(input("Hour of arrival : "))
m2 = int(input("Minute of arrival : "))

if h2 > h or m2 > m:
    if m2 > m:
        l = m2 - m
    print("Late")