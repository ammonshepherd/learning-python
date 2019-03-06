
## Exercise 7.11
## multiplication table
#  Write a program that prints a multiplication table for digits 1 to a certain
#  number num (you may assume for the output that num is one digit). A
#  multiplication table for the numbers 1 to num = 3 looks as follows:
#  . |  1  2  3 
#  ------------ 
#  1 |  1  2  3 
#  2 |  2  4  6 
#  3 |  3  6  9
#  So the labels on the rows are multiplied by the labels on the columns, and
#  the result is shown in the cell that is on that row/column combination.

#  Modified to ask for a number between 1 and 30.
print("Multiplication table!")
num = int( input("Enter a whole number between 1 and 30: ") )

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
    line = "{:>{w}}|".format(n, w=width)
    for p in range(1, num + 1):
        line += "{:>{w}}".format(n * p, w=width)
    print(line)

