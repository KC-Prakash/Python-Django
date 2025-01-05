def factorial(num1):
    if num1 == 0 or num1 == 1:
        return 1
    else:
        return num1 * factorial(num1 - 1)