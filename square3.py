userInput = input()
numList = [int(x) for x in userInput.split()]
list2 = []
for element in numList:
    list2.append(element ** 2)
    print(list2)