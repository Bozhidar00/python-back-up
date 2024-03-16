numbers_str = input("ЗАПИШИ ЧИСЛАТА С ПРАЗНО ПОЛЕ МЕЖДУ ВСЯКО: ")

numbers = numbers_str.split()
inverted_numbers = [str(-int(num)) if int(num) < 0 else str(-int(num)) for num in numbers]
print(inverted_numbers)