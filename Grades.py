grade = float(input())
def result(grade):
    if 2.00 <= grade >= 2.99:
        return "fail"
    elif 3.00 <= grade >= 3.49:
        return "poor"
    elif 3.50 <= grade >= 4.49:
        return "poor"
    elif 4.50 <= grade >= 5.49:
        return "poor"
    elif 5.50 <= grade >= 6.00:
        return "poor"


    print(result(grade))