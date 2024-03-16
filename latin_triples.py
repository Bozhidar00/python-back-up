N = int(input())

for i in range(N):
    for j in range(N):
        for k in range(N):
            first_letter = chr(ord('a') + i)
            second_letter = chr(ord('a') + j)
            third_letter = chr(ord('a') + k)

            print(f"{first_letter}{second_letter}{third_letter}")

print()
