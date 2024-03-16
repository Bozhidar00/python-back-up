import math

# Read input
group_size = int(input())
days = int(input())

# Initialize variables
total_coins = 0
companions_count = group_size

# Simulate the adventure
for day in range(1, days + 1):
    # Earn coins
    total_coins += 50 * companions_count

    # Spend coins for food
    total_coins -= 2 * companions_count

    # Organize a motivational party every 3rd day
    if day % 3 == 0:
        total_coins -= 3 * companions_count

    # Slay a boss monster every 5th day
    if day % 5 == 0:
        total_coins += 20 * companions_count
        # Spend additional coins if a party is organized on the same day
        if day % 3 == 0:
            total_coins -= 2 * companions_count

    # Two companions leave every 10th day
    if day % 10 == 0:
        companions_count -= 2

    # Five new companions join every 15th day
    if day % 15 == 0:
        companions_count += 5

# Calculate the number of coins each companion receives
coins_per_companion = total_coins // group_size

# Print the result
print(f"{companions_count} companions received {coins_per_companion} coins each.")
