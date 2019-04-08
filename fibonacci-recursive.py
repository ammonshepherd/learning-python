# Exercise 9.1 
# A recursive definition of the nth number of the Fibonacci sequence fib(n)
# states that fib(n) is equal to fib(n-1) + fib(n-2). Moreover, fib(1) and
# fib(2) are both 1. Write a recursive function that you can call with an
# integer argument n that returns the nth number of the Fibonacci sequence.

def nth(n):
    number = 0
    if n == 1 or n == 2:
        return 1
    number += nth(n-1) + nth(n-2)
    return number


def fib(num):
    sequence = ''
    count = 0
    while count < num:
        count += 1
        if count < 2:
            prev1 = 1
            prev2 = 0
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
        sequence += "{} ".format(current)
    return sequence

if __name__ == "__main__":
    print("The 7th number of the Fibonacci sequence is: ", end = '')
    print(nth(17))
    print("The whole sequence up to the 7th number is: ", end = '')
    print(fib(17))
