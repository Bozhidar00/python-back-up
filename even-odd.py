def sum_even_odd_digits(number):
    even_sum = 0
    odd_sum = 0

    for digit in str(number):
        digit_int = int(digit)
        if digit_int % 2 == 0:
            even_sum += digit_int
        else:
            odd_sum += digit_int

    result = f"Odd sum is {odd_sum}, Even sum is {even_sum}"
    return result

number = int(input("Enter a number: "))
result = sum_even_odd_digits(number)
print(result)
