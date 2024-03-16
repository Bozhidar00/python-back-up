numbers = input().split()
n = int(input())

numbers = [int(num) for num in numbers]
numbers.sort()

numbers = numbers[n:]

print(", ".join(map(str, numbers)))
