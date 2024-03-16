numbers = list(input())
squareNums = []

for i in numbers:
    square = lambda a : a**2
    squareNums.append(square(i))

    print(squareNums)