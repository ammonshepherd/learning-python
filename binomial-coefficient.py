def get_factorial(num):
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    return factorial


def get_coefficient(num1, num2):
    if num1 >= num2:
        result = get_factorial(num1) / (get_factorial(num2) * get_factorial(num1 - num2))
        return int(result)
    else:
        print("Error: The first number must be larger than the second number.")
        return False


if __name__ == "__main__":
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number smaller than the first: "))
    coeff = get_coefficient(num1, num2)
    if coeff:
        print("The binomial coefficient of {} and {} is {}".format(num1, num2, coeff))
    else:
        print("Try again.")



