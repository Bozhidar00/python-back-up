fire_ranges = {
    'High': range(81, 126),
    'Medium': range(51, 81),
    'Low': range(1, 51)
}

fire_cells_input = input().split('#')
water = int(input())

put_out_cells = []
total_effort = 0
total_fire_extinguished = 0

for cell in fire_cells_input:
    fire_type, fire_value = cell.split(' = ')
    fire_value = int(fire_value)

    if fire_value in fire_ranges[fire_type]:

        effort = 0.25 * fire_value

        if water >= fire_value:
            water -= fire_value
            put_out_cells.append(fire_value)
            total_effort += effort
            total_fire_extinguished += fire_value
        else:
            break

print("Cells:")
for cell in put_out_cells:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire_extinguished}")
