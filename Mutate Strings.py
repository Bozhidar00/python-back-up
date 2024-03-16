def mutate_strings(str1, str2):
    current_string = str1

    for i in range(len(str1)):
        if current_string != str2:
            print(current_string)
        current_string = current_string[:i] + str2[i] + current_string[i + 1:]

    if current_string != str2:  # Check if the last mutation is not equal to the target
        print(current_string)

# Examples
mutate_strings("bubble", "gum")
print("----------------")
mutate_strings("Kitty", "Doggy")
