key = int(input())

num_lines = int(input())

message = ""

is_upper = True

# Iterate through each line
for _ in range(num_lines):
    letter = input().strip()  # Remove leading/trailing whitespace

    # Decrypt the letter using the key
    decrypted_letter = chr(((ord(letter.lower()) - ord('a') + key) % 26) + ord('a'))

    if letter.isupper():
        decrypted_letter = decrypted_letter.upper()

    message += decrypted_letter

    is_upper = not is_upper

print(message)
