# Read input
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Initialize variables
helmet_breaks = 0
sword_breaks = 0
shield_breaks = 0
armor_breaks = 0

# Calculate the number of times each item gets broken
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        helmet_breaks += 1
    if fight % 3 == 0:
        sword_breaks += 1
    if helmet_breaks >= 2 and sword_breaks >= 2:
        shield_breaks += 1
        helmet_breaks -= 2
        sword_breaks -= 2
    if shield_breaks % 2 == 0:  # Consider shield breaks for armor
        armor_breaks += shield_breaks // 2

# Calculate expenses
total_expenses = (helmet_breaks * helmet_price +
                  sword_breaks * sword_price +
                  shield_breaks * shield_price +
                  armor_breaks * armor_price)

# Print the result
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
