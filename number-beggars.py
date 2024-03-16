def sum_for_beggars(values, n):
    sums = [0] * n  # sums for each beggar to 0
    for i, val in enumerate(values):
        sums[i % n] += val
        return sums


numbers = input().split(", ")
beggars_count = int(input())

numbers = [int(num) for num in numbers]

result = sum_for_beggars(numbers, beggars_count)

squared_result = list(map(lambda x: x**2, result))

print(squared_result)
