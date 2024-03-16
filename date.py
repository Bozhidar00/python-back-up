import calendar

def print_calendar(year):

    print(calendar.calendar(year))

year_input = input("Enter a year: ")

if year_input.isdigit():
    year = int(year_input)
    print_calendar(year)
else:
    print("Invalid input. Please enter a valid positive integer.")