# Exercise 12.5 The sieve of Eratosthenes is a method to find all prime numbers

def getPrimes(num):
    # Create the list of numbers
    numberRange = list(range(1, num + 1))
    # set the first number (one) to zero, since it can't be prime
    numberRange[0] = 0
    # loop through the whole list of numbers
    for n in range(1, len(numberRange)):
        # set the current number to a variable
        dot = numberRange[n]
        # if that number is zero already, then move to the next numbe# r
        if dot == 0:
            continue
        else:
            # loop through the whole list again, starting with the next number
            # in the list
            for i in range(n + 1, len(numberRange)):
                # set the value to a variable
                tod = numberRange[i]
                # if the number is zero, get the next number in the list
                if tod == 0:
                    continue
                # if the current number is divisible by the number in the outer
                # loop
                if tod % dot == 0:
                    # then change it to be zero
                    numberRange[i] = 0

    # create a new list to hold the prime numbers
    primeList = []
    # loop through the list of numbers
    for d in numberRange:
        # if the number is not zero
        if d != 0:
            # add it to the new list of prime numbers
            primeList.append(d)

    # return the list of primes
    return primeList


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print(getPrimes(num))
