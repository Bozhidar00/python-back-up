factor = int(input("Enter the factor: "))
count = int(input("Enter the count: "))

#списък, който съдържа множеството на факторът
multiples_list = [factor * i for i in range(1, count + 1)]

print(multiples_list)
