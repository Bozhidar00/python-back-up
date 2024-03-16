# for i in range(100, 0 , -1):
#     print(i)

# n = int(input())
# for i in range(1, n + 1, 3):
#     print(i, end  = "4")

# n = int(input())
# m = 7
# i = 0
# for n  in range(1 , n, 1):
#     if n % m == 0:
#         i += 1
#     #print(n)
# print(f"There are {i} numbers divisible with 7.")


# n = int(input())
# for i in range(n,0, -1):
#     print(i)


# t = input()
# for char in t:
#      print(char)


# a = 1
# e = 2
# i = 3
# o = 4
# u = 5

w = input()
a = ["a"]
e = ["e"]
i = ["i"]
o = ["o"]
u = ["u"]
sum = 0

for s in w:
    if s in a:
        sum =+ 1
    elif s in e:
        sum =+2
    elif s in i:
        sum =+ 3
    elif s in o:
        sum =+ 4
    elif s in u:
        sum =+ 5
print(sum)