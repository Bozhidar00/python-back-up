N = int(input())
total_sum = 0

for _ in range(N):
    char = input()
    total_sum += ord(char)

print(f"The sum equals: {total_sum}")
