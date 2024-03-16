
user_input = input("Enter a list of characters separated by ', ': ")

ascii_dict = {char: ord(char) for char in user_input.split(", ")}

print(ascii_dict)
