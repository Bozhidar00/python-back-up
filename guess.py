import random

def guess_the_number():
    correct_number = random.randint(1, 20)

    attempts = 0
    max_attempts = 5

    print("Добре дошли в играта за познаване на число!")
    print("За кое число си мисля?")

    while attempts < max_attempts:
        user_guess = input("Твоето предположение: ")

        # Validate that the input is a positive integer
        if not user_guess.isdigit():
            print("Невалидно! Моля въведете правилни числа.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess == correct_number:
            print(f"Поздравления! Ти позна числото {correct_number} за {attempts} опита.")
            break
        elif user_guess < correct_number:
            print("Не. Правилното число е по-голямо. Опитай отново!")
        else:
            print("Не. Правилното число е по-маклко. Опитай отново!")

    if attempts == max_attempts and user_guess != correct_number:
        print(f"Нямаш повече опити! Числото за което си мисля е {correct_number}.")

if __name__ == "__main__":
    guess_the_number()
