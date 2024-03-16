n = input()
ni = int(n)
sump = 0
sumn = 0

# while n != "stop":
#     n = input()
#     if n == "stop":
#         print(f"Sum of all prime numbers is : {sump}.")
#         print(f"Sum of all non prime numbers is : {sumn}.")
#         break
#     else:
#         pass
#     # ni = int(n)
#     if ni < 0:
#         print("Number is negative.")
#         pass
#     elif (ni%2) == 0:
#         sumn += ni
#     else:
#         sump += ni

for i in range(n):
    n = (input())
    if n == "stop":
        print(f"Sum of all prime numbers is : {sump}.")
        print(f"Sum of all non prime numbers is : {sumn}.")
        break
    else:
        pass
    ni = int(n)
    if ni < 0:
        print("Number is negative.")
        pass
    elif (ni%2) == 0:
        sumn += ni
    else:
        sump += ni