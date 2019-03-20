# Exercise 8.1
# Prints the multiplication table of a given number
# Accepts an integer between 1 and 30
# Returns a printed table of the multiplication table

def multiplication_table(num):
    if num < 20:
        width = 4
        dashes = "____"
    else:
        width = 6
        dashes = "______"

    topLine = '{:^{w}}|'.format("*", w=width)
    for n in range(1, num + 1):
        topLine +=  '{:>{w}}'.format(n, w=width)
    print(topLine)

    dashLine = '{:^{w}}'.format(dashes, w=width)
    for n in range(1, num + 2):
        dashLine +=  "{:>{w}}".format(dashes, w=width)

    print(dashLine)

    for n in range(1, num + 1):
        line = "{:^{w}}|".format(n, w=width)
        for p in range(1, num + 1):
            line += "{:>{w}}".format(n * p, w=width)
        print(line)

if __name__ == '__main__':
    print("Should print out the multiplication table for 9")
    multiplication_table(9)
