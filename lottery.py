import random
def generate_random_numbers():

    return random.sample(range(1, 36), 5)

random_numbers = generate_random_numbers()
print("Generated random numbers:", random_numbers)
