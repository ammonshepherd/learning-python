# Exercise 8.3 The Grerory-Leibnitz series approximates pi as 4 ∗ (1/1 − 1/3 +
# 1/5 − 1/7 + 1/9...). Write a function that returns the approximation of pi
# according to this series. The function gets one parameter, namely an integer
# that indicates how many of the terms between the parentheses must be
# calculated.

def approximate_pi(terms):
    number = 0
    for n in range(1, terms+1):
        denominator = int(2 * n - 1)
        if n > 1:
            fraction = 1 / denominator
            if n % 2 == 0:
                number -= fraction
            else:
                number += fraction
        else:
            number += 1 / denominator

    return (4 * number)

if __name__ == '__main__':
    print("using 1,000,000 terms pi is approximately")
    pi = approximate_pi(1000000)
    print(pi)
